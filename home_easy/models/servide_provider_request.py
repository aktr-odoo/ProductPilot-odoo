from odoo import models,fields,api
from odoo.exceptions import UserError
class ServiceProviderRequest(models.Model):
    _name = "service.provider.request"
    _description = "It's a service provider model"

    status  = fields.Selection([
        ('accepted','Accepted'),
        ('refused','Refused')
    ],
    copy=False,
    )
    # Relational Fields
    service_provider_id = fields.Many2one("service.provider")
    postcode = fields.Char(related='service_provider_id.postcode')
    customer_id = fields.Many2one("customer")
    service_type_ids = fields.Many2many("service.type")     
    seq_no = fields.Char(string="Task Reference",required=True,readonly=True,default = lambda self:('New'))               

    # Private Methods
    @api.model
    def create(self, vals):
        vals['seq_no'] = self.env['ir.sequence'].next_by_code('service.provider.request')
        return super(ServiceProviderRequest,self).create(vals)

    # Public methods
    def action_set_offer_accepted(self):
        for record in self:
            if record.service_provider_id.postcode == record.postcode and (record.service_type_ids in list(record.service_provider_id.service_type_ids)) :
                record.status = "accepted"
                record.service_provider_id.customer_ids += record.customer_id
            elif record.service_provider_id.postcode != record.postcode:
                raise UserError("The service provider dosen't provide service in postcode {}".format(record.postcode))
            else:
                raise UserError("The service provider doesn't provide the requested service type: {}".format(record.service_type_ids.name))
        return True
    
    def action_set_offer_refused(self):
        for record in self:
            record.status = "refused"
        return True