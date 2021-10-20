from odoo import api, fields, models


class SaleOrderInfor(models.Model):
    _inherit = 'sale.order'

    order_day_info = fields.Char('Order day')
    coupon = fields.Char('Discount Code')
    customer_email=fields.Char(related='partner_id.email',string='Customer Email')

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    shortcode = fields.Integer('Short_code')
    # product_id  = fields.Many2one('product.template', 'product category')
    cat = fields.Char('Category',related= 'product_id.product_tmpl_id.categ_id.name')
