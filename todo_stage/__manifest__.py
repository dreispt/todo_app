{
    'name': 'Add Stages and Tags to To-Dos',
    'description': 'Organize To-Do Tasks using Stages and Tags',
    'author': 'Daniel Reis',
    'depends': ['todo_app', 'mail'],
    'data': [
        # Ch04 Models
        'security/ir.model.access.csv',
        # Ch05 data Files
        'views/todo_menu.xml',
    ],
    # Ch05 Demo Data
    'demo': [
        'data/todo.task.csv',
        'data/todo_task.xml',
    ],
}
