from odoo import models,fields

class SerivceType(models.Model):
    _name = "service.type"
    _description = "It's a service type"
    _order = "sequence desc"

    name = fields.Char()
    color = fields.Integer()
    sequence = fields.Integer('Sequence',default="1")