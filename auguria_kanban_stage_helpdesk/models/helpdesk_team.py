# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models, _
import json


class HelpdeskTeam(models.Model):
    _inherit = "helpdesk.team"

    count_tickets_by_stages = fields.Char(string='Unassigned Tickets', compute='_compute_count_tickets_by_stages')

    def _compute_count_tickets_by_stages(self):
        for team in self:
            data = ''
            for stage in team.stage_ids:
                if stage.ag_is_display:
                    tickets_count = self.env['helpdesk.ticket'].search_count([
                        ('team_id', '=', team.id),
                        ('stage_id', '=', stage.id)
                    ])
                    data += str(stage.name) + '=' + str(tickets_count) + '#'
            team.count_tickets_by_stages = data[:-1]
