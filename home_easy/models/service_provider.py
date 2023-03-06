from odoo import models, fields,api

class ServiceProvider(models.Model):
    _name = "service.provider"
    _description = "It is a service provider module"
    _sql_constraints = [
        ("check_age","CHECK(age>18)","Your age must be grater to 18"),  
        ]
    _order = "name desc"
    # _inherits = {'customer':'customer_ids'}

    name = fields.Char()
    age = fields.Integer(default=19)
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
    default='available',
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
    color = fields.Integer()
    maid = fields.Boolean(default=False)
    baby_sitting = fields.Boolean(default=False)
    elderly_sitting = fields.Boolean(default=False)
    max_service = fields.Integer()

    # Relational Fields
    # service_type_ids = fields.Many2many("service.type")
    service_maid_ids = fields.Many2many("service.type.maid")
    service_baby_sitting_ids = fields.Many2many("service.type.baby.sitting")
    service_elderly_sitting_ids = fields.Many2many("service.type.elderly.sitting")
    customer_ids = fields.Many2many("customer",string="Assigned to")
    request_ids = fields.One2many("service.provider.request","service_provider_id")

    # ratings = fields.Float()
    # price = fields.Float() 
