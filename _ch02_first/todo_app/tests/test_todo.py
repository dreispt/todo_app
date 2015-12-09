# -*- coding: utf-8 -*-

from openerp.tests.common import TransactionCase
from openerp.exceptions import AccessError


class TestTodo(TransactionCase):

    def setUp(self, *args, **kwargs):
        result = super(TestTodo, self).setUp(*args, **kwargs)
        user_demo = self.browse_ref('base.user_demo')
        self.env= self.env(user=user_demo)
        return result

    def test_create(self):
        "Create a simple Todo."
        Todo = self.env['todo.task']
        # Create Test Task
        task = Todo.create({'name': 'Test Task'})
        self.assertEqual(task.is_done, False)
        # Test Toggle Done
        task.do_toggle_done()
        self.assertEqual(task.is_done, True)
        # Test Clear Done
        task.do_clear_done()
        self.assertEqual(task.active, False)

    def test_record_rule(self):
        "Test per user record rules"
        Todo = self.env['todo.task']
        task = Todo.sudo().create({'name': 'Admin Task'})
        with self.assertRaises(AccessError):
            Todo.browse([task.id]).name
