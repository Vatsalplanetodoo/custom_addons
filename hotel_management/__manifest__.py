# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'hotel_ERP',
    'version': '1.0',
    'author': 'Vatsal Thore',
    'category': 'hotel',
    'summary': 'Hotel info',
    'description': "Hotel",
    'website': 'https://www.odoo.com',
    'depends': [
        'base','stock','sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/room_info.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
