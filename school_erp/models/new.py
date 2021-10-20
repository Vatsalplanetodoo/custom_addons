from odoo import api, fields, models


class Newinherit(models.Model):
    _inherit = 'teacher.info'
    teacheridno = fields.Integer('Teacher id number')

from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    ci_product = fields.Selection([('person', 'Individual'),('company', 'Company')],'Company or Individual',related='partner_id.company_type')
    def _display_mto(self):
        self.order_line = self.env['weather1.info'].search([
            ('id', '=', self.id),
        ])




class Product(models.Model):
    _inherit = 'purchase.order.line'

    # product_id = fields.Many2one('product.product', string='Product', domain=[('purchase_ok', '=', True),('ci_product','=', 'partner_id.company_type')],
    #                              change_default=True)
    @api.onchange('product_qty')
    def _check_something(self):
        for record in self:
            if record.product_qty > 20:
                raise UserError(("Your product quantity is grater than 20 : %s" % record.product_qty))