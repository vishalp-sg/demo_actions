# -*- coding: utf-8 -*-

from odoo import models, fields,_,api

class Student(models.Model):
    _name = 'university.student'
    _description = 'University Student'

    name = fields.Char(string='Name')
    date_of_birth = fields.Date(string='Date of Birth')
    email = fields.Char(string='Email')
    classroom_id = fields.Many2one('university.classroom', string='Classroom')
    ref = fields.Char(string="Reference", default=lambda self: _('New'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('university.student')
        return super(Student, self).create(vals_list)

