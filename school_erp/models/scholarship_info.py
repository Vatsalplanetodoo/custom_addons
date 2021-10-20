from odoo import api, fields, models
class ScholasrshipInfo(models.Model):
    _name = 'scholarship.info'
    _rec_name = 'scholarship_name'
    student_name = fields.Char("Enter student name")
    standard_id = fields.Char("Enter Standard")


    division = fields.Selection([('div_a', 'A'),
                                 ('div_b', 'B'),
                                 ('div_c', 'C'),
                                 ('std_d', 'D'), ],
                                'Division')
    scholarship_name = fields.Char("Enter name of scholarship")
    scholarship_year = fields.Date("Enter the date of scholarship issued")







