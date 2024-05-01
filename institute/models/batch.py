from odoo import api,fields, models

class InstituteBatch(models.Model):
    _name = "institute.batch"
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

