from odoo import models, fields,api

class Customer(models.Model):
    _name = "customer"
    _description = "It is a service provider module"

    name = fields.Many2one("res.partner")
    age = fields.Integer()
    phone_number = fields.Char(copy=False,related="name.phone")
    email = fields.Char(related="name.email")
    address = fields.Char()
    profile_picture = fields.Image(copy=False)
    postcode =  fields.Char()
    color = fields.Integer()
    x = fields.Integer()
    # Address Fields
    street = fields.Char(related="name.street")
    street2 = fields.Char(related="name.street2")
    postcode = fields.Char(related="name.zip")
    city = fields.Char(related="name.city")
    state = fields.Char(related="name.state_id.name")
    country = fields.Char(related="name.country_id.name")
    country_code = fields.Char(related="name.country_code")
    
    # Relational Fields
    service_preferences_ids = fields.Many2many("service.type")
    service_request_ids = fields.One2many("service.provider.request","customer_id")
    # ratings = fields.Float()
