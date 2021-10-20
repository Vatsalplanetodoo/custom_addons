from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'
    ci_product = fields.Selection([('person', 'Individual'),
                                   ('company', 'Company')], 'Company or Individual', )

class ProductTemplate1(models.Model):
    _inherit = 'product.template'
    rent_ok = fields.Boolean('Can be rented')
    rent_price = fields.Float(
        'Rent Price', default=1.0,
        digits='Rent Price',
        help="Price at which the product is rented to customers.")
    # ci_product=fields.Selection([('person', 'Individual'),
    #                              ('company', 'Company')],'Company or Individual',)