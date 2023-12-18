# -*- coding: utf-8 -*-
{
    'name': 'pharmacie',
    'version': '2.0.0',
    'summary': 'mavou consulting',
    'sequence': -100,
    'description': """logiciel dedié au pharmacie""",
    'category': 'Tutorials',
    'author': 'ulrich',
  
    'depends': [
        'sale',
        'mail',
        'website_slides',
        'hr',
        
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
       
       'wizard/create_appointment_view.xml',
       'wizard/search_appointment_view.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/appointment_view.xml',
        'views/kids_view.xml',
        'views/patient_gender_view.xml',
        'views/sale.xml',
        'report/patient_details_template.xml',
        'report/patient_card.xml',
        'report/report.xml'
    ],
   
    'installable': True,
    'application': True,
    'auto_install': False,
}
