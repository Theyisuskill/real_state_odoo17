from odoo import models, fields, api, _

class StatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Real Estate Property Type'
    _order = 'name'
    
    name = fields.Char(string='Name', required=True)
    property_ids = fields.One2many('estate.property', 'property_type_id', string='Properties')
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'Name must be unique.')
    ]