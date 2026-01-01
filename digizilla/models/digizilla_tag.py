from odoo import models, fields


class DigizillaTag(models.Model):
    _name = 'digizilla.tag'
    _description = 'Digizilla Tag'
    _order = 'name'

    name = fields.Char(
        string="Tag Name",
        required=True,
        index=True,
    )

    color = fields.Integer(
        string="Color",
    )
