{
    'name': 'Real Estate account',
    'version': '1.0',
    'summary': 'Manage real estate properties and listings',
    'description': 'This module allows you to manage real estate properties and listings in Odoo.',
    'category': 'Real Estate',
    'author': 'Jesus Mendoza',
    'depends': ['base', 'sale', 'account','real_state'],
    'data': [
        'security/ir.model.access.csv',

        # 'views/listing_views.xml',
        # 'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}