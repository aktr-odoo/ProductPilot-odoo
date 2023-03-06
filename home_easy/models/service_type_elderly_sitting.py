from odoo import models,fields,api

class ServiceTypeElderlySitting(models.Model):
    _name = "service.type.elderly.sitting"
    _description = "It's a Elderly Sitting Service Type"

    name = fields.Char()
    color = fields.Integer()
    sequence = fields.Integer('Sequence',default="1")

    # # Relational Fields
    # provider_ids = fields.Many2many("service.provider")

