from odoo import models, fields, api, _, Command


class EstateProperty(models.Model):
    _inherit = 'estate.property'
    _description = 'Real Estate Property'
    
    def action_sold(self):
       
        su = super(EstateProperty, self).action_sold()
        
        move_type = 'out_invoice'
        

        # Create invoice
        self.env['account.move'].create({
            'partner_id': self.partner_id.id,
            'move_type': move_type,
            'invoice_line_ids': [
            Command.create( {
                'name': 'Sale Amount',
                'quantity': 1,
                'price_unit': self.price,
            }),
            Command.create( {
                'name': 'Administrative Expenses',
                'quantity': 1,
                'price_unit': 100.00,
            }),
            ],
        })

        # Perform any additional actions related to the invoice creation
        # ...

        # Return the result of the super method
        return su