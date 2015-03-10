# -*- coding: utf-8 -*-

from openerp import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'

    name = fields.Char()
    is_done = fields.Boolean()
    active = fields.Boolean(default=True)


class TodoTaskClear(models.TransientModel):
    _name = 'todo.task.clear'

    @api.multi
    def do_clear_done(self):
        Task = self.env['todo.task']
        done_recs = Task.search([('is_done', '=', True)])
        done_recs.active = False
        return True
