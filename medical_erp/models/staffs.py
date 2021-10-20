from odoo import api, fields, models


class Staffs(models.Model):
    _name = 'staffs.info'
    staff_name = fields.Char('Staff name')
    staff_id = fields.Integer('Staff ID')
    prod_sold = fields.Char('Product sold by')
    prod_type = fields.Selection([('equipments', 'Surgery equipments'),
                                  ('liquids', 'Liquids'),
                                  ('medicines', 'Medicines'),
                                  ('drugs', 'Medical Drugs'), ],
                                 'Stock_type', required=True)
    prod_sold_to = fields.Char('Prod sold to')
    sell_date = fields.Date('selling date')
