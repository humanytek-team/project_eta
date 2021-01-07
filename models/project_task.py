from odoo import api, fields, models, _


class ProjectTask(models.Model):
    _inherit = "project.task"

    date_deadline = fields.Date()
    remaining_hours_to_deadline = fields.Float(
        compute="_compute_remaining_hours_to_deadline",
    )

    def _compute_remaining_hours_to_deadline(self):
        for task in self:
            task.remaining_hours_to_deadline = 0
            if task.date_deadline:
                task.remaining_hours_to_deadline = (
                    (task.date_deadline - fields.Datetime.now()).total_seconds()
                    / 60
                    / 60
                )  # secods / minutes / hours
