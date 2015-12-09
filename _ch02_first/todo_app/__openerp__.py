{
    'name': 'To-Do Application',
    'description': 'Manage your personal To-Do tasks.',
    'author': 'Daniel Reis',
    'depends': ['base'],
    'application': True,
    'data': [
        'views/todo_view.xml',
        'views/todo_menu.xml',
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
    ]
}
