{
    'name': 'Indevit',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Modulo principal de Indevit',
    'description': """
        Indevit
        =======
        Modulo principal de Indevit con pantalla de bienvenida.
    """,
    'author': 'Indevit',
    'license': 'LGPL-3',
    'depends': ['base', 'web'],
    'data': [
        'views/indevit_dashboard_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'indevit/static/src/js/indevit_dashboard.js',
            'indevit/static/src/xml/indevit_dashboard.xml',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
