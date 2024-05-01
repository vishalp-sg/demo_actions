# -*- coding: utf-8 -*-

from odoo import fields, models


class CohortsFeesSku(models.Model):
    _name = 'cohorts.fees.sku'
    _rec_name = "name"
    _description = 'Cohorts Fees SKUs'

    name = fields.Char('Fees SKU')
