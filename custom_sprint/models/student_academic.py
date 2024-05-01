# -*- coding: utf-8 -*-

from odoo import exceptions, fields, models


class StudentAcademic(models.Model):
    _name = 'student.academic'
    _rec_name = "academicId"
    _description = 'Student Academic'

    academicId = fields.Char('Academic ID')
    university = fields.Char('University')
    institute = fields.Char('Institute')
    academic_name = fields.Char('Academic Name')
    graduation_qualifying_degree = fields.Char('Graduation Qualifying Degree')
    research_publication_title = fields.Char('Research Publicatio Title')
    graduation_discipline = fields.Char('Graduation Discipline')
    year_of_passing = fields.Char('Year of Passing')
    marks_scored = fields.Char('Marks Scored')
    total_marks = fields.Char('Total Marks')
    cgpa_gpa = fields.Char('CGPA/GPA')
    percentage = fields.Char('Percentage')
    attribute_type = fields.Char('Attribute Type')
    attribute_url = fields.Char('Attribute Url')
    student =  fields.Many2one('res.partner', 'Student')
