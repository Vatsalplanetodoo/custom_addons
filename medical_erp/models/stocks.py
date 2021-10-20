from odoo import api, fields, models
class Stocks(models.Model):
    _name = 'stocks.info'

    product = fields.Char('Product Name')

    mib = fields.Char('Product sold quantity')
    medicines = fields.Char('Product serial no')
    mit = fields.Char('Product delivered to')
    m_type = fields.Selection([('equipments', 'Surgery equipments'),
                                    ('liquids', ':Liquids'),
                                    ('medicines', 'Medicines'),
                                    ('drugs', 'Medical Drugs'),],
                                      'Stock_type', required=True)