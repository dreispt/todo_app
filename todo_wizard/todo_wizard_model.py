# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp import exceptions

import logging
_logger = logging.getLogger(__name__)


class TodoWizard(models.TransientModel):
    _name = 'todo.wizard'
    task_ids = fields.Many2many('todo.task', string='Tasks')
    new_user_id = fields.Many2one('res.users', string='Responsible to Set')
    new_deadline = fields.Date('Deadline to Set')

    @api.multi
    def do_mass_update(self):
        self.ensure_one()
        if not (self.new_deadline or self.new_user_id):
            raise exceptions.ValidationError('No data to update!')
        # else:
        _logger.debug('Mass update on Todo Tasks %s', self.tasks.ids)
        if self.new_deadline:
            self.task_ids.date_deadline = self.new_deadline
        if self.new_user_id:
            self.task_ids.user_id = self.new_user_id
        return True

    @api.multi
    def do_count_tasks(self):
        Task = self.env['todo.task']
        count = Task.search_count([])
        raise exceptions.Warning('There are %s active tasks.' % count)

    @api.multi
    def do_reopen_form(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,  # this model
            'res_id': self.id,  # the current wizard record
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new'}

    @api.multi
    def do_populate_tasks(self):
        self.ensure_one()
        Task = self.env['todo.task']
        all_tasks = Task.search([])
        self.task_ids = all_tasks
        # reopen the wizard form on the same record
        return self.do_reopen_form()
