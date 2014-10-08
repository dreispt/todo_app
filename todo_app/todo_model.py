from openerp import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)

    @api.one
    def set_toggle_done(self):
        self.is_done = not self.is_done

    @api.multi
    def do_inactivate_if_done(self):
        done_recs = self.search([('is_done', '=', True)])
        if done_recs:
            done_recs.write({'active': False})
            return {
                'warning': {
                    'title': 'Information',
                    'message': '%d tasks purged.' % len(done_recs)
                }
            }
