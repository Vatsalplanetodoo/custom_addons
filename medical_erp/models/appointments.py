from odoo import api, fields, models, http
from odoo.http import request


class Staffs(models.Model):
    _name = 'appointments.info'
    _rec_name = 'patient'
    patient = fields.Char('Patient name')
    age = fields.Integer('Age')
    # date = fields.Char('Date of appointment')
    date1 = fields.Date('Date of appointment')
    reg_note = fields.Char('Registration note')
    name_id = fields.Many2one('hospitals.info','Hospital name')

