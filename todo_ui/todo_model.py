from openerp import models, fields
from openerp.addons.base.res.res_request import referencable_models


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
    _name = 'todo.tag'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char('Name', size=30, translate=True)
    #tasks0 = fields.Many2many('')
    tasks = fields.Many2many('todo.task', string='Tasks')


class TodoTask(models.Model):
    _inherit = 'todo.task'

    # Relational fields
    stage = fields.Many2one('todo.stage', 'Stage')
    tags = fields.Many2many('todo.tag', string='Tags')

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
