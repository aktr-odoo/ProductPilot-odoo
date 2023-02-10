from odoo import models, fields

class Customer(models.Model):
    _name = "Customer"
    _description = "It is a service provider module"

    name = fields.Char(required=True)
    age = fields.Integer(required=True)
    qualifications = fields.Char()
    experience = fields.Float(required=True)
    phone_number = fields.Integer(required=True,copy=False)
    email = fields.Char()
    address = fields.Char()
    profile_picture = fields.Image(required=True,copy=False)
    service_preferences = fields.Selection([
        ('maid','Miad'),
        ('baby_sitter','Baby Sitting'),
        ('elderly_sitting','Elderly Sitting')
    ])
    # ratings = fields.Float()
    # price = fields.Float(required=True) 