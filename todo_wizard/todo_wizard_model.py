from openerp import models, fields, api
from openerp import exceptions

import logging
_logger = logging.getLogger(__name__)


class TodoWizard(models.TransientModel):
    _name = 'todo.wizard'
    tasks = fields.Many2many('todo.task', string='Tasks')
    new_user_id = fields.Many2one('res.users', string='Set Responsible')
    new_deadline = fields.Date('Set Deadline')

    @api.one
    def do_mass_update(self):
        if not self.new_deadline and not self.new_user_id:
            raise exceptions.ValidationError('No data to update!')
        _logger.debug('Mass update on Todo Tasks %s' % self.tasks.ids)
        for task in self.tasks:
            if self.new_deadline:
                task.date_deadline = self.new_deadline
            if self.new_user_id:
                task.user_id = self.new_user_id
