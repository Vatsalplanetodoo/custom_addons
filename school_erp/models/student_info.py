from odoo import api, fields, models


class StudentInfo(models.Model):
    _name = 'student.info'

    name = fields.Char('Name',required=True)
    middle_name = fields.Char('Middle Name')
    last_name = fields.Char('Last Name')
    full_name = fields.Char('Full Name',compute='_compute_full_name',store=True)
    student_age = fields.Integer('Age')
    quota = fields.Selection([('five','5%'),
                                        ('ten', '10%'),
                                        ('two-five', '25%'),
                                        ('twelve', '12%'),
                                        ('fifty', '50%'),
                                        ],'Education Quota')
    # student_std = fields.Selection([('std_1', 'Standard 1'),
    #                                 ('std_2', 'Standard 2'),
    #                                 ('std_3', 'Standard 3'),
    #                                 ('std_4', 'Standard 4'),],
    #                                   'Standard', required=True)


    city = fields.Char('City', default ='Mumbai', readonly =True)
    gender_male = fields.Selection([('male', 'Male'),
                                    ('female', 'Female')],
                                   'Gender', required=True)
    is_pwd = fields.Boolean('Is Phycially Handiacpped?')
    standard_id = fields.Many2one('standard.info', 'Standard')
    division = fields.Selection([('div_a', 'A'),
                                 ('div_b', 'B'),
                                 ('div_c', 'C'),
                                 ('std_d', 'D'),],
                                'Division', related= 'standard_id.division')
    teacher_name = fields.Char(related= 'standard_id.teacher_name')
    student_id = fields.Many2one(comodel_name='standard.info', string='Student Id', )
    sports_id = fields.Many2one(comodel_name='sports.activity', string='Game') #domain=[('sports_type', '=', 'indoor')])

    # library_ids = fields.One2many(comodel_name='library.info', inverse_name='book_name', string='library')

    issue_date = fields.Datetime('Issue date')
    return_date = fields.Datetime('Return date')

    student1_id = fields.Many2one(comodel_name='library.info')
    fest_ids = fields.Many2many(comodel_name='cultural.fest', relation= 'student_info_cultural_fest_rel', column1='stud_id', column2='fest_id', string='fest events')
    scholarship_ids = fields.Many2many(comodel_name='scholarship.info', relation='student_info_scholarship_info_rel',
                                       column1='stud_id', column2='scholarship_id', string='scholarship')

    teacher_ids = fields.One2many(comodel_name='teachers.subjects.line', inverse_name='teacher1_id')
    # male_id = fields.Many2one(comodel_name='male.info')

    budget = fields.Integer('Budget')

    # event_id=fields.Many2one(comodel_name='competition.fees')
    event_ids=fields.One2many(comodel_name='competition.fees',inverse_name='name_id')

    chemistry=fields.Integer('Chemistry')
    physics=fields.Integer('Physics')
    maths=fields.Integer('Maths')
    english=fields.Integer('English')
    hsc_total=fields.Integer('Hsc Total',compute='_compute_total_marks',store=True)
    hsc_percent=fields.Float('Hsc percent',readonly=True ,store=True)
    status=fields.Selection([('pass','Pass'),
                                 ('fail','Fail'),],)
    documents = fields.Binary(string='Upload your file')
    timetable =fields.Html('Time Table')

    # @api.depends('event_ids')
    # def _compute_inherited_class(self):
    #     for rec in self.event_ids:
    #         if rec.fees_calc==False:
    #             rem = self.budget - rec.fees_amount
    #             self.budget = rem
    #             rec.fees_calc=True
    @api.onchange('hsc_total')
    def _percentage(self):
        self.hsc_percent= 100 * self.hsc_total / 400
        if self.hsc_percent <40:
            self.status='fail'
        elif self.hsc_percent>40:
            self.status='pass'



    def change_age(self):
        self.student_age = 25
        return 0

    @api.onchange('is_pwd')
    def onchange_quota(self):
        print("aaaaaaaa")
        if self.is_pwd == True:
            self.quota = 'two-five'
        else:
            self.quota = 'ten'

    @api.depends('name', 'middle_name','last_name')
    def _compute_full_name(self):
        print('in compute')
        if self.name and self.middle_name and self.last_name:
            self.full_name = self.name+" "+self.middle_name+" "+self.last_name

    @api.depends('chemistry', 'physics','english','maths')
    def _compute_total_marks(self):
        print('in compute')
        if self.chemistry and self.physics and self.english and self.maths:
            self.hsc_total = self.chemistry + self.physics + self.english + self.maths


class TeachersSubjects(models.Model):
    _name = 'teachers.subjects.line'

    teacher1_id = fields.Many2one(comodel_name='student.info')
    subject_id = fields.Many2one(comodel_name='subjects.info', string="Subjects")
    teacher_name_id = fields.Many2one(comodel_name='teacher.info')

