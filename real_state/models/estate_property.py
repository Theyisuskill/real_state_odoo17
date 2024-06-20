from odoo import models, fields, api, _
from odoo.exceptions import UserError


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'
    _order = 'id desc'
    
    
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=fields.Date.add(fields.Date.today(),months=+3))
    expected_price = fields.Float(string='Price')
    selling_price = fields.Float()
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ])
    active = fields.Boolean(default=True)
    partner_id = fields.Many2one('res.partner', string='Salesman')
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    property_type_id = fields.Many2one('estate.property.type', string='Property Types')
    tax_ids = fields.Many2many("account.tax", string="Taxes")
    estate_property_offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')
    total_area = fields.Integer(string='Total Area', compute='_compute_total_area', store=True)
    best_price = fields.Float(string='Best Price', compute='_compute_best_price', store=True)   
    state = fields.Selection([
        ('new', 'New'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], default='new')   
    property_tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    res_user_id = fields.Many2one('res.users', string='Responsible')
    
    _sql_constraints = [
        ('positive_expected_price', 'CHECK(expected_price >= 0)', 'Expected price must be strictly positive.'),
        ('positive_selling_price', 'CHECK(selling_price >= 0)', 'Selling price must be positive.'),
    ]
    @api.depends('expected_price', 'estate_property_offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = record.expected_price
            for offer in record.estate_property_offer_ids:
                if offer.status == 'accepted' and offer.price > record.best_price:
                    record.best_price = offer.price
    
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
            
    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 1000
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False
            
    def action_cancel(self):
        self.state = 'canceled'
        
    def action_sold(self):
        if self.state == 'canceled':
            raise UserError(_('You cannot sell a canceled property'))
        self.state = 'sold'
        
    @api.constrains('selling_price', 'expected_price')
    def _check_selling_price(self):
        for record in self:
            if record.selling_price < record.expected_price * 0.9:
                raise UserError(_('Selling price cannot be lower than 90% of the expected price'))
            
    @api.ondelete(at_uninstall=False)
    def _prevent_deletion(self):
        if self.state not in ['new', 'canceled']:
            raise UserError(_('You cannot delete a property that is not in "New" or "Canceled" state'))
        
    