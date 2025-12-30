from odoo import models, fields
import base64

class Digizilla(models.Model):
    _name = 'digizilla.digizilla'
    _description = 'Digizilla'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], tracking=True)
    country_id = fields.Many2one('res.country', tracking=True)
    joining_date = fields.Date(tracking=True)
    tag_ids = fields.Many2many('res.partner.category', tracking=True)
    customer_ids = fields.Many2many('res.partner', string='Customers', tracking=True)
    company_id = fields.Many2one('res.company', required=True, tracking=True)
    notes = fields.Text()
    comments = fields.Char()

    pdf_file = fields.Binary("PDF File")
    pdf_filename = fields.Char("PDF Filename")

    def action_print_pdf(self):
        self.ensure_one()
        return self.env.ref('digizilla.digizilla_report').report_action(self)

    def action_save_pdf(self):
        self.ensure_one()
        pdf = self.env.ref('digizilla.digizilla_report')._render_qweb_pdf(self.id)[0]
        self.pdf_file = base64.b64encode(pdf)
        self.pdf_filename = f"{self.name}.pdf"
