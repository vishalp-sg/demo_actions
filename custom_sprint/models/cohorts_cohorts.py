# -*- coding: utf-8 -*-

from odoo import fields, models


class CohortsCohorts(models.Model):
    _name = 'cohorts.cohorts'
    _rec_name = "batchId"
    _description = 'Cohorts'

    batchId = fields.Char('Batch ID')
    salesFrom = fields.Date('Sales From')
    salesTo = fields.Date('Sales To')
    deliveryStarts = fields.Date('Delivery Start')
    deliveryEnds = fields.Date('Delivery End')
    platformValidity = fields.Date('Platform Validity')
    calendarId = fields.Char('Calendar ID')
    category = fields.Char('Category')
    primary_sku_ids = fields.Many2many('cohorts.sku', 'cohorts_primary_sku_rel', 'cohorts_id', 'sku_id', 'Primary SKUs')
    secondary_sku_ids = fields.Many2many('cohorts.sku', 'cohorts_secondary_sku_rel', 'cohorts_id', 'sku_id', 'Secondary SKUs')
    fees_sku_ids = fields.Many2many('cohorts.fees.sku', 'cohorts_fees_sku_rel', 'cohorts_id', 'fees_sku_id', 'Fees SKUs')
    students =  fields.Many2many('res.partner', string='Students')
