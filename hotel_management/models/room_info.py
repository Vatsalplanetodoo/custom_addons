from odoo import api, fields, models
import datetime
from odoo.exceptions import ValidationError


class RoomInfo(models.Model):
    _name = 'room.info'
    _rec_name = 'roomNumber'

    roomNumber=fields.Integer('Room number') #10 rooms in 5 floors
    floorNumber=fields.Integer('Floor')
    verificationdone=fields.Boolean('Verification Done')

    @api.onchange('roomNumber')
    def check_rno(self):
        if self.roomNumber :
            if self.roomNumber>10:
                raise ValidationError('There are only 10 rooms')

    @api.onchange('floorNumber')
    def check_fno(self):
        if self.floorNumber:
            if self.floorNumber >5 :
                raise ValidationError('There are only 5 floors')


class OtherExpenses(models.Model):
    _inherit = 'res.partner'
    # product, quantity and price filed
    otherex_ids =fields.One2many(comodel_name='cust.exp',inverse_name='product_id')

class OthExp(models.Model):
    _name = 'cust.exp'
    product = fields.Many2one(comodel_name='product.product',string='Product')
    product_id = fields.Many2one(comodel_name='res.partner')
    quantity = fields.Integer('Quantity')
    price = fields.Integer('price')
    uom_qty=fields.Many2one(comodel_name='uom.uom')



class SaleC(models.Model):
    _inherit = 'sale.order'
    ver_done=fields.Boolean('Verification Done')
    roomno = fields.Many2one(comodel_name='room.info',string='room number')

    def action_confirm(self):
        res = super(SaleC, self).action_confirm()
        if self.state == "sale":
            return {
                'name':("Create Invoices"),
                'view_mode': 'form',
                'view_type': 'form',
                'view_id': False,
                'res_model': 'sale.advance.payment.inv',
                'type': 'ir.actions.act_window',
                'target': 'new'
            }

    @api.onchange('partner_id')
    def update_det(self):
        print('update')
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.partner_id.otherex_ids:
                val = {
                    'product_id': line.product.id,
                    'product_uom_qty': line.quantity,
                    'price_unit': line.price,
                    'product_uom':line.uom_qty,
                }
                lines.append((0, 0, val))
                print(lines)
            rec.order_line = lines
            return 0

    global reserve_rn
    reserve_rn = []
    @api.onchange('roomno')
    def reserve_rno(self):
        for rec in self.roomno:
            print(rec.roomNumber)
            if rec.roomNumber in reserve_rn:
                raise ValidationError('Room no is Occupied')
            else:
                reserve_rn.append(rec.roomNumber)
            print(reserve_rn)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    # checkin = fields.datetime('Checkin time')
    checkin1 = fields.Datetime('Checkin time')
    # checkout = fields.datetime('Checkout time')
    checkout1 = fields.Datetime('Checkout time')
    noofperson=fields.Integer('No of person')
    hrsstay=fields.Integer('No of hours stay',compute='_duration',store=True)
    # stay=fields.Integer('Time of stay',compute='_duration',store=True)


    @api.depends('checkin1', 'checkout1')
    def _duration(self):
        if self.checkin1 and self.checkout1:
            start_time = self.checkin1
            close_time = self.checkout1
            if self.checkout1 > self.checkin1:
                diff = close_time - start_time
                days, seconds = diff.days, diff.seconds
                hours = days * 24 + seconds // 3600
                self.hrsstay = hours
                if hours > 0 and hours<=24:
                    self.product_uom_qty=1
                else:
                    self.product_uom_qty=diff.days
            else:
                raise ValidationError('Checkout date should be superior than start day')
            # d1 = datetime.datetime.strptime(str(start_time), fmt)
            # d2 = datetime.datetime.strptime(str(close_time), fmt)
            #
            # diff = str(d2 - d1)
            # self.hrsstay = int(diff[:2])*24







