from odoo import api, fields, models

class SaleComp(models.Model):
    _inherit = 'sale.order'
    company_check=fields.Boolean('Company check')

    @api.onchange('partner_id')
    def _selectedpart(self):

        if self.partner_id.is_company == True:
            self.company_check =True
        else:
            self.company_check=False

    tax_discount = fields.Selection([('ten', '10%'),#nouse
                                  ('five', '5%'),],
                                 'Tax Discount',)
    tot_discount = fields.Integer('Discount',readonly=True)#nouse
    tot_discount1 = fields.Float('Discount',readonly=True)



    @api.onchange('discount')
    def discount(self):
        if self.discount == 5:
            self.tot_discount1 = self.discount
        elif self.discount == 10:
            self.tot_discount1 = self.discount
        return 0

