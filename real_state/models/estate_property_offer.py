from odoo import models, fields, api, _

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Real Estate Property Offer'
    _order = 'price desc'
    
    price = fields.Float(string='Price')
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    ], copy=False, string='Status')
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('estate.property', string='Property', required=True)
    deadline = fields.Datetime(string='Deadline', compute='_compute_deadline', store=True, default=fields.Datetime.now)
    validaty = fields.Integer(string='Validaty (in days)')
    
    _sql_constraints = [
        ('positive_price', 'CHECK(price >= 0)', 'Price must be strictly positive.'),
    ]
    
    @api.depends('create_date', 'validaty')
    def _compute_deadline(self):
        for record in self:
            record.deadline = fields.Datetime.add(fields.Datetime.today(), days=+record.validaty)
            
    def action_accept(self):
        self.status = 'accepted'

    def action_refuse(self):
        self.status = 'refused'
        
  