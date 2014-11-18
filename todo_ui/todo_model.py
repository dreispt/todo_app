from openerp import models, fields, api
from openerp.addons.base.res.res_request import referencable_models
import datetime

class Stage(models.Model):
    _name = 'todo.stage'
    name = fields.Char(
        string='Name',
        help='The title for the stage.',
        readonly=False,
        required=True,
        index=True,
        copy=False,
        default='New',
        # states
        # groups
    )
    desc = fields.Text('Description')
    fold = fields.Boolean('Folded?')
    sequence = fields.Integer('Sequence')
    perc_complete = fields.Float('% Complete', (3, 2))
    state = fields.Selection(
        [('draft', 'New'), ('open', 'Started'), ('done', 'Closed')],
        'State'
    )
    # Date, Datetime
    # HTML
    # Binary, Sparse?
    tasks = fields.One2many('todo.task', 'stage', 'Tasks in this stage')

    # Computed:
    # compute
    # inverse
    # search
    # store


class Tags(models.Model):
    _name = 'todo.task.tag'
    _parent_store = True
    # _parent_name = 'parent_id'
    name = fields.Char('Name', size=30)
    parent_id = fields.Many2one('todo.task.tag', 'Parent Tag')

    tasks = fields.Many2many('todo.task', string='Tasks')


class TodoTask(models.Model):
    _inherit = 'todo.task'

    # Relational fields
    stage = fields.Many2one('todo.stage', 'Stage')
    tags = fields.Many2many('todo.task.tag', string='Tags')

    state = fields.Selection(
        string='Stage State',
        related='stage.state',
        store=True,
    )

    refers_to = fields.Reference(
        [('res.user', 'User'), ('res.partner', 'Partner')],
        #referencable_models,  # selection=
        'Refers to',  # string=
    )

    user_email = fields.Char(
        'user email',
        compute='_compute_user_email',
        store=True)

    @api.one
    def _compute_user_email(self):
        self.user_email = self.user_id.email

    days_deadline = fields.Integer(
        'Days to deadline',
        compute='_compute_days_deadline')

    @api.one
    def _compute_days_deadline(self):
        if self.date_deadline:
            d1 = fields.Date.from_string(self.date_deadline)
            d0 = fields.Date.from_string(fields.Date.today())
            delta = d1 - d0
            print 'compute', self, self.date_deadline, delta.days
            #import pudb; pudb.set_trace()
            self.days_deadline = delta.days
