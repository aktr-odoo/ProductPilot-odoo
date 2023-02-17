from odoo import models, fields

class ServiceProvider(models.Model):
    _name = "service.provider"
    _description = "It is a service provider module"

    name = fields.Char()
    age = fields.Integer()
    qualifications = fields.Char()
    experience = fields.Float()
    skills = fields.Char()
    phone_number = fields.Integer(copy=False)
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
    profile_picture = fields.Image(copy=False)
    postcode = fields.Char()

    # Relational Fields
    service_type_ids = fields.Many2many("service.type")
    customer_ids = fields.Many2many("customer",string="Assigned to")
    request_ids = fields.One2many("service.provider.request","service_provider_id")
    # ratings = fields.Float()
    # price = fields.Float() 