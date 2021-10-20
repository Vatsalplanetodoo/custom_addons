from odoo import api, fields, models
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

class VendorAcc(models.Model):
    _inherit = 'account.move'

    cust_comp=fields.Char('Individual or Company')
    @api.onchange('partner_id')
    def check_p(self):
        if self.partner_id.is_company==True:
            self.cust_comp="company"
        elif self.partner_id.is_company==False:
            self.cust_comp="Individual"
    def unlink(self):#overrides delete option
        if self.amount_total>=10000:
            raise ValidationError("Cannot delete record containing total more than 10000")
        return super(VendorAcc, self).unlink()

class AccReg(models.TransientModel):
    _inherit = 'account.payment.register'

    def action_create_payments(self):
        account_active_id = self.env['account.move'].search([('id', '=', self.env.context.get('active_id'))])


        if account_active_id.cust_comp == "company" and self.amount <= 1000:
            raise ValidationError(("Minimum amount must be 1000"))
        else:
            payments = self._create_payments()

        if self._context.get('dont_redirect_to_payments'):
            return True

        action = {
            'name': _('Payments'),
            'type': 'ir.actions.act_window',
            'res_model': 'account.payment',
            'context': {'create': False},
        }
        if len(payments) == 1:
            action.update({
                'view_mode': 'form',
                'res_id': payments.id,
            })
        else:
            action.update({
                'view_mode': 'tree,form',
                'domain': [('id', 'in', payments.ids)],
            })
        return action