# -*- coding: utf-8 -*-
{
    "name": "Telent Sprint Customisation",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "summary": "Telent Sprint Customisation",
    'category': 'Server Tools',
    "author": "Umang Gajjar<umangg113@gmail.com>",
    "website": "http://awsomellc.com",
    "depends": [
        "base", "contacts", "crm"
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/crm_views.xml',
        'views/cohorts_cohorts_views.xml',
        'views/sku_views.xml',
    ],
    'demo': [
        'demo/webhook_demo.xml',
    ],
    "demo": [],
    "application": False,
    "development_status": "Beta",
}
