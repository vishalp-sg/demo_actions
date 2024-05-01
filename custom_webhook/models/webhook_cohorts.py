# -*- coding: utf-8 -*-

from odoo import exceptions, fields, models
import json
import ast


class WebhookCohorts(models.Model):
    _name = 'webhook.cohorts'
    _rec_name = "batchId"
    _description = 'Webhook Cohorts'

    method = fields.Selection([
        ('POST', 'POST'),
        ('GET', 'GET'),
    ])
    batchId = fields.Char('Batch ID')
    request = fields.Char('Request')
    params = fields.Text('Params')
    response = fields.Char('Response')
    status = fields.Selection([
        ('success', 'Success'),
        ('failed', 'Failed')
    ], 'Status')
    is_store = fields.Boolean('Is Store', default=False)
    cohort = fields.Many2one('cohorts.cohorts', 'Cohorts')

    def update_cohort_vals(self, cohort_vals, field_value, key, value):
        if str(field_value) != value:
            cohort_vals.update({key: value})
        return  cohort_vals

    def execute(self):
        objCohorts = self.env['cohorts.cohorts']
        objCohortsSku = self.env['cohorts.sku']
        for rec in self.filtered(lambda r: not r.is_store and r.status == 'success'):
            vals = ast.literal_eval(rec.response)
            cohort = objCohorts.search([('batchId', '=', rec.batchId)], limit=1)
            if cohort:
                cohort_vals = {}
                cohort_vals = self.update_cohort_vals(
                    cohort_vals,
                    cohort.salesFrom,
                    'salesFrom',
                    vals['salesFrom']
                )

                cohort.write(cohort_vals)
            else:
                lst_primary_sku = []
                for p_sku in list(set(vals.get('primarySKUs'))):
                    primary_sku = objCohortsSku.search([('name', '=', p_sku)], limit=1)
                    if not primary_sku:
                        primary_sku = objCohortsSku.create({'name': p_sku})
                    lst_primary_sku.append((4, primary_sku.id))

                secondarySKUs = []
                for s_sku in list(set(vals.get('secondarySKUs'))):
                    secondary_sku = objCohortsSku.search([('name', '=', s_sku)], limit=1)
                    if not secondary_sku:
                        secondary_sku = objCohortsSku.create({'name': s_sku})
                    secondarySKUs.append((4, secondary_sku.id))

                feesSKUs = []
                for f_sku in list(set(vals.get('applicationFeeSKUs'))):
                    fees_sku = self.env['cohorts.fees.sku'].search([('name', '=', f_sku)], limit=1)
                    if not fees_sku:
                        fees_sku = self.env['cohorts.fees.sku'].create({'name': f_sku})
                    feesSKUs.append((4, fees_sku.id))

                cohort = objCohorts.create({
                    'batchId': vals.get('batchId'),
                    'salesFrom': vals.get('salesFrom'),
                    'salesTo': vals.get('salesTo'),
                    'deliveryStarts': vals.get('deliveryStarts'),
                    'deliveryEnds': vals.get('deliveryEnds'),
                    'platformValidity': vals.get('platformValidity'),
                    'calendarId': vals.get('calendarId'),
                    'category': vals.get('category'),
                    'fees_sku_ids': feesSKUs or False,
                    'primary_sku_ids': lst_primary_sku or False,
                    'secondary_sku_ids': secondarySKUs or False
                })

            if cohort:
                rec.write({'is_store': True, 'cohort': cohort.id})
