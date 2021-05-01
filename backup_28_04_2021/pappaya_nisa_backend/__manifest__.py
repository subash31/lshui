# -*- coding: utf-8 -*-
{
    'name': 'Pappaya NISA Backend Module',
    'version': '14.0.2.4.0',
    'license': 'LGPL-3',
    'category': 'PappayaEd',
    "sequence": 1,
    'summary': 'Manage User registration and environment URLs',
    'complexity': "easy",
    'description': """
        Description    ======
    """,
    'author': 'Think42Labs',
    'website': 'http://www.think42labs.com',
    'depends': ['web','base','website'],
    'data': [
        #'security/ir.model.access.csv',
        'views/nisa_backend_view.xml',
        # Template
        'template/nisa_home_page.xml',
        'template/nisa_styles.xml',
        'template/nisa_industrial.xml',
        'template/nisa_minimal.xml',
        'template/nisa_minimal.xml',
        'template/nisa_pop.xml',
        'template/nisa_urban.xml',
    ],
    'qweb': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
