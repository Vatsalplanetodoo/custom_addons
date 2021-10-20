from odoo import api, fields, models, http
from odoo.http import request

class App(http.Controller):
    @http.route('/appointment_webform', type="http",auth="public",website=True)
    def app_webform(self, **kw):
        print("Execution here")
        return http.request.render('medical_erp.create_appointment', {})

    @http.route('/create/webappointment', type="http",auth="public",website=True)
    def create_webappointment(self, **kw):
        print("Data received")
        request.env['appointment.info'].sudo().create(kw)
        return request.render("medical_erp.patient_thanks")
