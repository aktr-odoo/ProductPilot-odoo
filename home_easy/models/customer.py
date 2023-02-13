from odoo import models, fields

class Customer(models.Model):
    _name = "customer"
    _description = "It is a service provider module"

    name = fields.Char(required=True)
    age = fields.Integer(required=True)
    # qualifications = fields.Char()
    # experience = fields.Float(required=True)
    phone_number = fields.Integer(required=True,copy=False)
    email = fields.Char()
    address = fields.Char()
    profile_picture = fields.Image(required=True,copy=False)
    service_preferences = fields.Many2many("service.type",required=True)
    postcode =  fields.Char(required=True)
    # ratings = fields.Float()