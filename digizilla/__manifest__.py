{
    'name': 'Digizilla Management',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Manage Digizilla records',
    'depends': ['base', 'mail', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/digizilla_views.xml',
        'reports/digizilla_report.xml',
        'reports/digizilla_report_template.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'digizilla/static/src/js/hide_create.js'
        ]
    },
    'application': True
}