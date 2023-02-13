from odoo import models,fields

class SerivceType(models.Model):
    _name = "service.type"
    _description = "It's a service type"

    name = fields.Char(required=True)