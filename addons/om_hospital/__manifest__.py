{
    'name':'hospital management systeme',
    'author':'ulrich',
    'website':'odoo.tech',
    'sumary':'odoo16 Development',
    'depends':['mail'],
    'data':[
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml'
    ],
    'development_status': 'alpha',
    'application': True,
    
    'installable': True,
     'test': True,  # Activation des tests automatiques
}