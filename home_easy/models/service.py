from odoo import models, fields

class Service(models.Model):
    _name = "service"
    _description = "It provides service types"

    name = fields.Char(required=True)
    description = fields.Char()
    price = fields.Float(required=True)