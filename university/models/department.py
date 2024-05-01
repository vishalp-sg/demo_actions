# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Department(models.Model):
    _name = 'university.department'
    _description = 'University Department'

    name = fields.Char(string='Name')

