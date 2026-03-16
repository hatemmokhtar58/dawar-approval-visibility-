{
    'name': 'Dawar Approval Visibility',
    'version': '1.0',
    'summary': 'Control visibility of approval categories based on user groups',
    'description': """
        This module adds a field to Approval Category to restrict visibility 
        to specific user groups. If no groups are selected, the category is visible to everyone.
    """,
    'category': 'Approvals',
    'author': 'HWZN',
    'depends': ['approvals'],
    'data': [
        'security/ir_rule.xml',
        'views/approval_category_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
