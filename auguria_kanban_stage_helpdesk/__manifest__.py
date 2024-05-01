# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': "Kanban Stage in Helpdesk",
    'description': """
        This module allow you to add the number of ticket in the different stages of each helpdesk team in the kanban 
        view 
    """,
    'author': 'Auguria SAS',
    'license': 'OPL-1',
    'website': 'https://www.auguria.fr',
    'support': 'contact@auguria.fr',
    'category': 'Uncategorized',
    'version': '15.0.1',
    'depends': ['base', 'helpdesk'],
    'images': ['static/description/banner.png'],
    'data': [
        'views/helpdesk_team_view_kanban.xml',
        'views/helpdesk_stage_form_view.xml',
    ],
}
