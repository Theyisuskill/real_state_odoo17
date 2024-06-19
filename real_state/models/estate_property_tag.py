from odoo import models, fields, api, _

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Real Estate Property Tag'
    _order = 'name'
    
    name = fields.Char(string='Name', required=True)
    color = fields.Integer()
    property_ids = fields.Many2one('estate.property', string='Properties')