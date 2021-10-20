from odoo import api, fields, models

class CulturalFest(models.Model):
    _name = 'cultural.fest'
    _rec_name = 'fest_name'

    fest_name = fields.Char('Festival Name')
    standard_id = fields.Many2one('standard.info','Standard Name')
    number_of_participants = fields.Integer('Number of Participants')
    festival_information =fields.Text('Fest Information')

    competition_ids = fields.One2many(comodel_name='competition.fees', inverse_name='comp_id')

    @api.model
    def default_get(self, fields):
        res = super(CulturalFest,self).default_get(fields)
        res['fest_name'] = 2
        res['number_of_participants']= '10'
        return res



class CompetitionFees(models.Model):
    _name = 'competition.fees'
    _rec_name = 'fees_amount'

    competition = fields.Char('Competition')
    fees_amount = fields.Integer('Fees Amount')
    name_id = fields.Many2one(comodel_name='student.info',string='Name')
    comp_id=fields.Many2one(comodel_name='cultural.fest')
    # fees_paid=fields.Boolean('Fees Paid')
    fees_calc=fields.Boolean('Fees Calculation')


    @api.onchange('fees_amount')
    def onchange_fees_id(self):
        print("onchange running")
        if self.fees_amount:
            self.name_id.budget = self.name_id.budget - self.fees_amount
            self.fees_calc = True

    def unlink(self):
        print("Unlink is running")
        for record in self:
            print(record)
            for rec in record.name_id:
                print(rec.budget)
                budget_remained = rec.budget + record.fees_amount
                rec.budget = budget_remained
        return super(CompetitionFees, self).unlink()







