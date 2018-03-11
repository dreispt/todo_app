from datetime import date
from odoo.tests.common import TransactionCase
from odoo import fields
from odoo.exceptions import Warning


class TestWizard(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestWizard, self).setUp(*args, **kwargs)
        # Close any open Todo tasks
        self.env['todo.task']\
            .search([('is_done', '=', False)])\
            .write({'is_done': True})
        # Demo user will be used to run tests
        demo_user = self.env.ref('base.user_demo')
        Todo = self.env['todo.task'].sudo(demo_user)
        # Create two Todo tasks to use in tests
        t0 = date.today()
        self.todo1 = Todo.create({
            'name': 'Todo1',
            'user_id': demo_user.id,
            'date_deadline': fields.Date.to_string(t0),
            })
        self.todo2 = Todo.create({
            'name': 'Todo2',
            'user_id': demo_user.id,
            })
        # Create Wizard instance to use in tests
        Wizard = self.env['todo.wizard'].sudo(demo_user)
        self.wizard = Wizard\
            .with_context(active_ids=None)\
            .create({})

    def test_populate_tasks(self):
        """Populate tasks button should add two tasks"""
        self.wizard.do_populate_tasks()
        count = len(self.wizard.task_ids)
        self.assertEqual(
            count, 2,
            'Expected 2 populated tasks')

    def test_mass_change(self):
        """Mass change deadline date"""
        self.wizard.do_populate_tasks()
        self.wizard.new_deadline = self.todo1.date_deadline
        self.wizard.do_mass_update()
        self.assertEqual(
            self.todo1.date_deadline,
            self.todo2.date_deadline)

    def test_count(self):
        """Test count button"""
        with self.assertRaises(Warning) as e:
            self.wizard.do_count_tasks()
        self.assertIn(' 2 ', str(e.exception))
