# -*- coding: utf-8 -*-

from odoo import exceptions, fields, models


class StudentEmployer(models.Model):
    _name = 'student.employer'
    _rec_name = "employerId"
    _description = 'Student Employer'

    employerId = fields.Char('Employer ID')
    employer_name = fields.Char('Employer Name')
    type_of_organisation = fields.Char('Organisation Type')
    job_title = fields.Char('Job Title')
    working_since = fields.Char('Working Since')
    working_till = fields.Char('Working Till')
    functional_area = fields.Char('Functional Area')
    nature_of_occupation = fields.Char('Occupation')
    occupational_fields = fields.Char('Occupational Fields')
    presently_working = fields.Char('Presently Working')
    gross_pay_per_annum = fields.Char('Gross Pay / Annum')
    employment_status = fields.Char('Employment Status')
    attribute_type = fields.Char('Attribute Type')
    attribute_url = fields.Char('Attribute Url')
    student =  fields.Many2one('res.partner', 'Student')
