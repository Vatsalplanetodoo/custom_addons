# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'School ERP',
    'version': '1.0',
    'author': 'Vatsal Thore',
    'category': 'Tutorials',
    'summary': 'Tutorials of school ERP',
    'description': "We are learning what is odoo and development in odoo",
    'website': 'https://www.odoo.com',
    'depends': [
        'base','sale','account','medical_erp','purchase','product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/student_info_views.xml',
        'views/standard_info_views.xml',
        'views/teacher_info_views.xml',
        'views/sports_activity_views.xml',
        'views/library_info_views.xml',
        'views/cultural_fest_views.xml',
        'views/scholarship_info_views.xml',
        'views/subject_info_views.xml',
        'views/sale_order_views.xml',
        'views/product_template1_views.xml',
        'views/weather1_info_views.xml',
        'wizard/update_age_wizard_views.xml',
        'views/account_vendor_views.xml',
        'views/sale_comp_views.xml',
        'views/new_views.xml',
        'reports/student_card.xml',
        'reports/report.xml',
        'reports/sale_report_inherit.xml',


    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
