from openerp import models, fields, api
from openerp import exceptions




class TodoWizard(models.TransientModel):
    _name = 'todo.wizard'
    new_user = fields.Many2one('res.users', string='Set Responsible')
    new_deadline = fields.Date('Set Deadline')
    tasks = fields.Many2many('todo.task', string='Tasks')

    @api.one
    def button_test(self):
        print "Entering interactive debugger."
        print "Press 'h' for help, 'c' to continue."
        result = True
        from pprint import pprint as pp  # noqa
        import pdb; pdb.set_trace()  # noqa
        return result

    @api.one
    def do_populate(self):
        Todo = self.env['todo.task']
        all_todos = Todo.search([])
        #self.tasks = all_todos
        # Reopen wizard
        action = {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            #'res_id': self.id,
            'res_model': 'todo.wizard', #self._name,
            'target': 'new',
        }
        print action
        return self.env.ref('todo_app.action_todo_wizard')
        return action


    @api.one
    def do_mass_update(self):
        if not self.new_deadline and not self.new_user:
            raise exceptions.ValidationError('No data to update!')
        for task in self.tasks:
            if self.new_deadline:
                task.date_deadline = self.new_deadline
            if self.new_user:
                task.user_id = self.new_user
