from openerp import models, fields, api
from openerp.addons.base.res import res_request


class Tag(models.Model):
    _name = 'todo.task.tag'
    name = fields.Char('Name', size=40, translate=True)

    # Many2many inverse relation
    tasks = fields.Many2many('todo.task', string='Tasks')

    # Hierarchic relations:
    _parent_store = True
    _parent_name = 'parent_id'  # the default
    parent_id = fields.Many2one('todo.task.tag', 'Parent Tag')
    # parent_left = fields.Integer('Parent Left', index=True)
    # parent_right = fields.Integer('Parent Right', index=True)
    child_ids = fields.One2many('todo.task.tag', 'parent_id', 'Child Tags')


class Stage(models.Model):
    _name = 'todo.task.stage'
    _order = 'sequence,name'
    _rec_name = 'name'  # the default
    _table_name = 'todo_task_stage'  # the default

    # Field attributes:
    name = fields.Char(
        string='Name',
        # Common field attributes:
        copy=False,
        default='New',
        groups="base.group_user,base.group_no_one",
        help='The title for the stage.',
        index=True,
        readonly=False,
        required=True,
        states={'done': [('readonly', False)]},
        # String only attributes:
        size=40,
        translate=True,
    )

    # Other string fields:
    desc = fields.Text('Description')
    state = fields.Selection(
        [('draft', 'New'), ('open', 'Started'), ('done', 'Closed')],
        'State',
    )
    docs = fields.Html('Documentation')

    # Numeric fields:
    sequence = fields.Integer('Sequence')
    perc_complete = fields.Float('% Complete', (3, 2))

    # Date fields:
    effective_date = fields.Date('Effective Date')
    write_date = fields.Datetime('Last Changed')

    # Other fields:
    fold = fields.Boolean('Folded?')
    image = fields.Binary('Image')

    # One2many inverse relation:
    tasks = fields.One2many('todo.task', 'stage', 'Tasks in this stage')


class TodoTask(models.Model):
    _inherit = 'todo.task'

    # Relational fields
    stage = fields.Many2one('todo.task.stage', 'Stage')
    tags = fields.Many2many(
        'todo.task.tag',      # related= (model name)
        'todo_task_tag_rel',  # relation= (table name)
        'task',               # column1= ("this" field)
        'tag',                # column2= ("other" field)
        string='Tags',

        # Relational field attributes:
        auto_join=False,
        context={},
        domain=[('parent_id', '!=', False)],
        ondelete='cascade',
        ### domain=['|', ('effective_date','=',False), ('effective_date','<=',)],
    )
    # Dynamic Reference fields:
    refers_to = fields.Reference(
        # Set a Selection list, such as:
        # [('res.user', 'User'), ('res.partner', 'Partner')],
        # Or use standard "Referencable Models":
        res_request.referencable_models,
        'Refers to',  # string= (title)
    )

    state = fields.Selection(
        string='Stage State',
        related='stage.state',
        store=True,
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
