{
    'name': 'Todo Tasks',
    'version': '1.0',
    'summary': 'My first custom module',
    'description': """
        هذا الموديول مثال لتعلم كيفية عمل Module في Odoo.
        يمكنك إضافة Models و Views هنا.
    """,
    'author': 'Salah',
    'category': 'Tools',
    'depends': ['base', 'mail','contacts'],
    'assets': {

    },
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/tasks_view.xml',
        'reports/task_report.xml',








    ],
    'demo': [

    ],

    'application': True,
'installable': True,
}
