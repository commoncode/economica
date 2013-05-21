vhosts = {
    'economica': {
        'hosts': ['economica.commoncode.com.au'],
        'manage': './manage.py',
        'settings': 'economica.settings.production',
        'requirements': 'requirements/production.txt'
    },

    # Staging
    'economica.commoncode.com.au': {
        'hosts': ['economica.commoncode.com.au'],
        'manage': './manage.py',
        'settings': 'economica.settings.staging',
        'requirements': 'requirements/staging.txt'
    }
}
