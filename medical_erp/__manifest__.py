# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Medical ERP',
    'version': '1.0',
    'author': 'Vatsal Thore',
    'category': 'pharmacy',
    'summary': 'Pharmacy',
    'description': "medical ecosystem",
    'website': 'https://www.odoo.com',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hospitals_views.xml',
        'views/staffs_views.xml',
        'views/stocks_views.xml',
        'views/appointments_views.xml',
        # 'views/website_form.xml',


    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
