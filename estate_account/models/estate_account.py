from odoo import models, fields, api, _

class EstateAccount(models.Model):
    _name = 'estate.account'
    _description = 'Real Estate Account'
    
    name = fields.Char(string='Name', required=True)