# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    leadId = fields.Char(string='Lead ID')
    ownerId = fields.Char(string='Owner ID')
    lead_owner_name = fields.Char(string='Owner Name')
    linkedin = fields.Char(string='LinkedIn')

    cohort_name = fields.Char(string='Cohort Name')
    cohort_program_parent_account = fields.Char(string='Cohort Program Parent Account')
    cohort_program = fields.Char(string='Cohort Program')
    cohort_applied = fields.Char(string='Cohort Applied')

    program = fields.Char(string='Program')
    program_and_location = fields.Char(string='Program and Location')
    landing_page = fields.Char(string='Landing Page')
    status = fields.Char(string='Status')

    def action_student(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("custom_sprint.action_students")
        action['domain'] = [('id', 'in', self.partner_id.ids)]
        action['view_mode'] = 'form'
        action['target'] = 'current'
        action['context'] = {
            'active_test': False,
            'create': False
        }
        return action
        return action
