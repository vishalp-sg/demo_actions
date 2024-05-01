from odoo import models, fields


class Professor(models.Model):
    _name = 'university.professor'
    _description = 'University Professor'

    name = fields.Char(string='Name')
    date_of_birth = fields.Date(string='Date of Birth')
    email = fields.Char(string='Email')
    department_id = fields.Many2one('university.department', string='Department')