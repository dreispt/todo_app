from odoo import api, fields, models


class TodoTask(models.Model):
    _name = 'todo.task'

    name = fields.Char(help="What needs to be done?")
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
    date_deadline = fields.Date('Deadline')
    user_id = fields.Many2one(
        'res.users',
        string='Responsible',
        default=lambda s: s.env.user)
    team_ids = fields.Many2many('res.partner', string='Team')

    @api.multi
    def do_clear_done(self):
        for task in self:
            task.active = False
        return True

    @api.multi
    def write(self, values):
        # Before write logic
        if 'active' not in values:
            values['active'] = True
        return super(TodoTask, self).write(values)
