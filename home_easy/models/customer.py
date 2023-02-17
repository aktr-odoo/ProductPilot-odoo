from odoo import models, fields

class Customer(models.Model):
    _name = "customer"
    _description = "It is a service provider module"

    name = fields.Char()
    age = fields.Integer()
    phone_number = fields.Integer(copy=False)
    email = fields.Char()
    address = fields.Char()
    profile_picture = fields.Image(copy=False)
    postcode =  fields.Char()
    
    # Relational Fields
    service_preferences_ids = fields.Many2many("service.type",)
    # ratings = fields.Float()