from odoo import models, fields, api
from odoo.exceptions import UserError

class DigizillaRecord(models.Model):
    _name = 'digizilla.record'
    _description = 'Digizilla Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    record_id = fields.Many2one('digizilla.record', string="Record")

    name = fields.Char(string="Name", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    country_id = fields.Many2one('res.country', string="Country", tracking=True)
    joining_date = fields.Date(string="Joining Date", tracking=True)
    company_id = fields.Many2one('res.company', string="Company", tracking=True, default=lambda self: self.env.company)
    tags = fields.Many2many('digizilla.tag', string="Tags")
    notes = fields.Text(string="Notes")
    comments = fields.Text(string="Comments")

    # -------------------
    # Automatic Logging
    # -------------------
    @api.model
    def create(self, vals):
        record = super(DigizillaRecord, self).create(vals)
        self.env['digizilla.log'].create({
            'name': f"Created record: {record.name}",
            'note': f"Record {record.name} was created.",
        })
        return record

    def write(self, vals):
        res = super(DigizillaRecord, self).write(vals)
        for record in self:
            changes = ", ".join(f"{k}={v}" for k,v in vals.items())
            self.env['digizilla.log'].create({
                'name': f"Updated record: {record.name}",
                'note': f"Record {record.name} updated: {changes}",
            })
        return res

    def unlink(self):
        for record in self:
            self.env['digizilla.log'].create({
                'name': f"Deleted record: {record.name}",
                'note': f"Record {record.name} was deleted.",
            })
        return super(DigizillaRecord, self).unlink()


    # -----------------------------
    # PDF Report
    # -----------------------------
    
    def action_print_pdf(self):
        return self.env.ref('digizilla.action_digizilla_report').report_action(self)
