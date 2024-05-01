from odoo import models,fields


class School(models.Model):
    _name = 'school.student'
    _description = "School Records"

    name = fields.Many2one('res.partner',string='Student')
    class_id = fields.Integer(string='class')
    division = fields.Char(string='Division')