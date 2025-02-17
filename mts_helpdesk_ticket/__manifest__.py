# -*- coding: utf-8 -*-
{
    'name': "Support Ticket Management",

    'description': """
        Save the incidents that occurred to customers and assign them to a user to solve them.
    """,
    'author': "Javier Alfonso González de Zayas",
    'website': "",
    'category': 'HelpDesk',
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
