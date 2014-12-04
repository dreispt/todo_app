from openerp import models, fields, api


class TodoWizard(models.TransientModel):
    _name = 'todo.wizard'
    new_user = fields.Many2one('res.users', string='Set Responsible')
    new_deadline = fields.Date('Set Deadline')
    tasks = fields.Many2many('todo.task', string='Tasks')

    @api.one
    def button_test(self):
        print "Entering interactive debugger."
        print "Press 'h' for help, 'c' to continue."
        from pprint import pprint as pp
        import pdb; pdb.set_trace()
