from odoo import models, fields, api, _

class ResUser(models.Model):
    _inherit = 'res.users'
    _description = 'Res User'
    
    estate_property_ids = fields.One2many('estate.property', 'res_user_id', string='Properties')