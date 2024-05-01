# -*- coding: utf-8 -*-
from odoo import models, fields


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    message_id = fields.Many2one('mail.message', string='Message Id')
    feedback_ratings = fields.Float(string='Feedback Ratings')
    model = fields.Char(string='Model')
    res_id = fields.Integer(string='Res Id')
