from odoo import models,fields,api

class ServiceProviderRequest(models.Model):
    _name = "service.provider.request"
    _description = "It's a service provider model"
    # not working, doubt
    # _sql_constraints = [
    #     ('check_postcode','CHECK(postcode == service_provider_id.postcode)','The service provider which you are requesting is not available at your Postcode')
    #     ]

    status  = fields.Selection([
        ('accepted','Accepted'),
        ('refused','Refused')
    ],
    copy=False,
    )
    postcode = fields.Char()
     
    # Relational Fields
    service_provider_id = fields.Many2one("service.provider",)
    customer_id = fields.Many2one("customer",)
    service_type_ids = fields.Many2many("service.type")

    def action_set_offer_accepted(self):
        for record in self:
            record.status = "accepted"
            record.service_provider_id.customer_ids = record.customer_id
        return True
    
    def action_set_offer_refused(self):
        for record in self:
            record.status = "refused"
        return True


        