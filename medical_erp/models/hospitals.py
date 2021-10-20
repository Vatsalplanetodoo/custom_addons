from odoo import api, fields, models
from datetime import datetime

class Hospitals(models.Model):
    _name = 'hospitals.info'

    name = fields.Char('Hospital Name')
    address = fields.Char('Address')
    hospital_id = fields.Char('Hospital id')
    # stocks_o = fields.Char('stocks ordered')
    stocks_o1 = fields.Integer('stocks ordered')
    order_date = fields.Date('Order date')
    ord_received = fields.Selection([('yes','YES'),
                                     ('no','NO')],
                                    'Y/N',required=True)
    stocks_ids = fields.One2many(comodel_name='stocks.info', inverse_name='m_type', string='Stocks')

    @api.model
    def create(self, vals):
        _inherit = 'hospitals.info'
        print('CREATE CALL', vals)
        print('Create working')
        vals['order_date'] = datetime.today()
        return super(Hospitals, self).create(vals)