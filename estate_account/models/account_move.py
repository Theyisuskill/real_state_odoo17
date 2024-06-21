from odoo import models, fields, api, _

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    estate_property_id = fields.Many2one('estate.property', string='Property')
    estate_property_offer_id = fields.Many2one('estate.property.offer', string='Offer')
    
    def action_post(self):
        res = super(AccountMove, self).action_post()
        if self.estate_property_id:
            self.estate_property_id.write({'state': 'sold'})
        return res