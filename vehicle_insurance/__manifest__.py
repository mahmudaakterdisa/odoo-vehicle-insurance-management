{
    'name': 'Vehicle Insurance Management',
    'version': '1.0',
    'summary': 'Manage vehicle insurance policies and claims',
    'author': 'Disa',
    'category': 'Insurance',
    'depends': ['base','calendar', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/actions.xml',
        'views/menus.xml',
        'views/customer_views.xml',
        'views/policy_views.xml',
        'views/claim_views.xml',
    ],
    'installable': True,
    'application': True,
}
