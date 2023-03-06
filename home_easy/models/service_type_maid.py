from odoo import models,fields

class SerivceTypeMaid(models.Model):
    _name = "service.type.maid"
    _description = "It's a maid service type"
    _order = "sequence desc"

    name = fields.Char()
    color = fields.Integer()
    sequence = fields.Integer('Sequence',default="1")

    # Relational Fields
    provider_ids = fields.Many2many("service.provider")