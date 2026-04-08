
from odoo import fields, models


class Task(models.Model):
    _name = 'task'
    _description = 'Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    task_name = fields.Char(tracking=True)
    assign_to = fields.Char(string="Assign To", tracking=True)
    description = fields.Text(string="Description", tracking=True)
    due_date = fields.Date(string="Due Date", tracking=True)
    status = fields.Selection(
        selection=[('new', 'New'), ('inprogress', 'In Progress'), ('done', 'Done')],
        string="Status",
        default='new',
        tracking=True,
    )
