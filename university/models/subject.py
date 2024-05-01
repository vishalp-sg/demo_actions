from odoo import models, fields

class Subject(models.Model):
    _name = 'university.subject'
    _description = 'University Subject'

    name = fields.Char(string='Name')
    department = fields.Char(string='Department')
    credits = fields.Integer(string='Credits')
    prerequisites = fields.Many2many(
        'university.subject',  # Destination model (self-referencing)
        'subject_prerequisites_rel',  # Custom table name
        'subject_id',  # Field on this model
        'prerequisite_id',  # Field on the other model
        string='Prerequisites'
    )
