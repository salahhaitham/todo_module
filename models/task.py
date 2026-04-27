from email.policy import default

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Task(models.Model):
    _name = 'task'
    _description = 'Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'task_name'

    task_name = fields.Char(tracking=True,required=True)
    task_lines_ids=fields.One2many(
        'task.lines', 'task_id'
    )
    estimate_time = fields.Float(string="Estimated Time")
    assign_to_id = fields.Many2one(
        'res.partner', )
    description = fields.Text(string="Description", tracking=True)
    due_date = fields.Date(string="Due Date", tracking=True)
    active = fields.Boolean(default=True)
    is_late=fields.Boolean(default=False)
    status = fields.Selection(
        selection=[('new', 'New'), ('inprogress', 'In Progress'), ('done', 'Done')],
        string="Status",
        default='new',
        tracking=True,
    )
    total_time = fields.Float(
        string="Total Time",
        compute="_compute_total_time",
        store=True
    )



    def check_date_validator(self):
        task_ids=self.search([])
        for task in task_ids:
            if task.due_date and task.due_date < fields.Date.today():
                task.is_late=True

    @api.constrains('total_time', 'estimate_time')
    def _check_time_limit(self):
        for record in self:
            if record.total_time > record.estimate_time:
                raise ValidationError("Total time cannot exceed estimated time.")

    @api.depends('task_lines_ids.line_time_takes')
    def _compute_total_time(self):
        for task in self:
            task.total_time = sum(task.task_lines_ids.mapped('line_time_takes'))

    def task_state_new(self):
        for task in self:
            task.status='new'

    def task_state_inprogress(self):
        for task in self:
            task.status = 'inprogress'
    def task_state_done(self):
        for task in self:
            task.status = 'done'

    _sql_constraints = [('unique_name','unique (task_name)','name is unique')]

class TaskLines(models.Model):
    _name = 'task.lines'
    _description = 'Task Lines'
    task_id = fields.Many2one("task")
    line_description = fields.Char(string="Description")
    line_time_takes = fields.Float(string="Time Takes")


