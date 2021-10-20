from odoo import api, fields, models


class TeacherInfo(models.Model):
    _name = 'teacher.info'
    _rec_name = 'name'
    name = fields.Char('Teacher Name')
    Surname = fields.Char('Surname')
    standard =fields.Integer("standard")
    division = fields.Selection([('div_a', 'A'),
                                 ('div_b', 'B'),
                                 ('div_c', 'C'),
                                 ('div_d', 'D'), ],
                                'Division', required=True)


    city = fields.Char('City', default ='Mumbai', readonly =True)
    gender = fields.Selection([('male', 'Male'),
                                    ('female', 'Female')],
                                      'Gender', required=True)
    is_pwd = fields.Boolean('is available fulltime ')

    sub_id = fields.Many2one('subjects.info',"subject")
    stud_id =fields.Many2one('student.info')

class Subjects(models.Model):

    _name = 'subjects.info'
    _rec_name = 'sub'
    sub = fields.Char("subject")



