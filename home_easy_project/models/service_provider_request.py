from odoo import models,fields,Command

class ServiceProviderRequest(models.Model):
    _inherit = "service.provider.request"

    def action_set_offer_accepted(self):
        name = self.customer_id.name.name
        self.env['project.project'].create({
            'name':name
        })
        return super(ServiceProviderRequest,self).action_set_offer_accepted()
