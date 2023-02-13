from odoo import models, fields

class ServiceProvider(models.Model):
    _name = "service.provider"
    _description = "It is a service provider module"

    name = fields.Char(required=True)
    age = fields.Integer(required=True)
    qualifications = fields.Char()
    experience = fields.Float(required=True)
    skills = fields.Char()
    phone_number = fields.Integer(required=True,copy=False)
    email = fields.Char()
    address = fields.Char()
    availability = fields.Selection([
        ('available','Available'),
        ('not available','Not available')
    ],
    default='available'
    )
    description = fields.Char()
    maratial_status = fields.Selection([
            ('single','Single'),
            ('married','Married'),
            ('widowed','Widowed'),
            ('divorced','Divorced'),
            ('separated','Separated')
        ],
        default='single'
        )
    profile_picture = fields.Image(required=True,copy=False)
    # service_type = fields.Selection([
    #     ('maid','Miad'),
    #     ('baby_sitter','Baby Sitting'),
    #     ('elderly_sitting','Elderly Sitting')
    # ])
    service_type = fields.Many2many("service.type",required=True)
    postcode = fields.Char(required=True)

    # ratings = fields.Float()
    # price = fields.Float(required=True) 