# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import models, fields, api, _


class HelpdeskStage(models.Model):
    _inherit = 'helpdesk.stage'

    ag_is_display = fields.Boolean(
        string=_('Show on kanban'),
        default=False,
        help=_('check the checkbox if you want to display the data of the this stape on kanban view')
    )
