{
    'name': 'Real Estate Management',
    'version': '1.0',
    'summary': 'Manage real estate properties and listings',
    'description': 'This module allows you to manage real estate properties and listings in Odoo.',
    'category': 'Real Estate',
    'author': 'Jesus Mendoza',
    'depends': ['base', 'sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/res_user_view_inherit.xml',
        'views/state_menu.xml',

        # 'views/listing_views.xml',
        # 'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}