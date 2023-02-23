from odoo import models, fields

class Customer(models.Model):
    _name = "customer"
    _description = "It is a service provider module"

    name = fields.Many2one("res.partner")
    age = fields.Integer()
    phone_number = fields.Integer(copy=False)
    email = fields.Char()
    address = fields.Char()
    profile_picture = fields.Image(copy=False)
    postcode =  fields.Char()
    color = fields.Integer()
    
    # Relational Fields
    service_preferences_ids = fields.Many2many("service.type")
    service_request_ids = fields.One2many("service.provider.request","customer_id")
    # ratings = fields.Float()