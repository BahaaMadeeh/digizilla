{
    'name': 'Digizilla Records',
    'version': '1.0',
    'summary': 'Manage Digizilla members',
    'description': 'Complete Digizilla module with kanban, tree, form and PDF report',
    'author': 'Bahaa Madeeh',
    'category': 'Tools',
    'depends': ['base', 'mail', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/digizilla_views.xml',
        'views/digizilla_menus.xml',
        'reports/digizilla_report_template.xml',
        'reports/digizilla_report.xml',
        
    ],
    'assets': {
        'web.assets_backend': [
            'digizilla/static/src/js/hide_create_button.js',
        ],
    },
    'installable': True,
    'application': True,
}
