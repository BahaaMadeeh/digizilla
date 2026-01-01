from odoo import models, fields


class DigizillaRecord(models.Model):
    _name = 'digizilla.record'
    _description = 'Digizilla Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string="Name",
        tracking=True,
    )

    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')],
        string="Gender",
        tracking=True,
    )

    country_id = fields.Many2one(
        'res.country',
        string="Country",
        tracking=True,
    )

    joining_date = fields.Date(
        string="Joining Date",
        tracking=True,
    )

    company_id = fields.Many2one(
        'res.company',
        string="Company",
        tracking=True,
        default=lambda self: self.env.company,
    )

    tags = fields.Many2many(
    comodel_name='digizilla.tag',
    relation='digizilla_record_tag_rel',
    column1='record_id',
    column2='tag_id',
    string="Tags",
    )


    notes = fields.Text(
        string="Notes",
    )

    comments = fields.Text(
        string="Comments",
    )

    def action_print_pdf(self):
        return self.env.ref(
            'digizilla.action_digizilla_report'
        ).report_action(self)

