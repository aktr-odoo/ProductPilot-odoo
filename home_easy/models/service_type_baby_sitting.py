from odoo import models,fields,api

class ServiceTypeBabySitting(models.Model):
    _name = "service.type.baby.sitting"
    _description = "It's a Baby Sitting Service Type"

    name = fields.Char()
    color = fields.Integer()
    sequence = fields.Integer('Sequence',default="1")

    # # Relational Fields
    # provider_ids = fields.Many2many("service.provider")

    