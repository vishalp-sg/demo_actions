from odoo import models, fields,_,api

class Classroom(models.Model):
    _name = 'university.classroom'
    _inherit = 'mail.thread'
    _description = 'University Classroom'

    name = fields.Char(string='Name')
    room_number = fields.Char(string='Room Number')
    building_name = fields.Char(string='Building Name')
    capacity = fields.Integer(string='Capacity')
    professor_id = fields.Many2one('university.professor', string='Professor')
    ref = fields.Char(string="Reference", default=lambda self: _('New'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('university.classroom')
        return super(Classroom, self).create(vals_list)


