# -*- coding: utf-8 -*-
{
    "name": "Telent Sprint Webhook",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "summary": "Telent Sprint Webhook",
    'category': 'Server Tools',
    "author": "Umang Gajjar<umangg113@gmail.com>",
    "website": "http://awsomellc.com",
    "depends": [
        "base", "web", "custom_sprint"
    ],
    'external_dependencies': {
        'python': [
            'ipaddress',
            'requests',
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/webhook_views.xml',
        'views/webhook_cohorts_views.xml',
        'views/webhook_leads_views.xml',
    ],
    'demo': [
        'demo/webhook_demo.xml',
    ],
    "demo": [],
    "application": False,
    "development_status": "Beta",
}
