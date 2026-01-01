
from odoo import models, fields

class DigizillaLog(models.Model):
    _name = 'digizilla.log'         
    _description = 'Digizilla Log'

    name = fields.Char(string='Description', required=True)
    date = fields.Datetime(string='Date', default=fields.Datetime.now)
    description = fields.Text(string='Notes')
    record_id = fields.Many2one('digizilla.record', string="Record")
    action = fields.Char(string="Action")
