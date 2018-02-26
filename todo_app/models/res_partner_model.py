from odoo import models, fields


class TodoTask(models.Model):
    _inherit = 'res.partner'

    todo_ids = fields.Many2many('todo.task', string='Team')
