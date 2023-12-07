{
    'name':'patient',
    'author':'ulrich',
    'website':'odoo.tech',
    'sumary':'odoo16 Development',
    'depends':['mail'],
    'data':[
        'views/menu.xml',  
        'views/patient.xml'
    ],
    'development_status': 'alpha',
    'application': True,
    
    'installable': True,
     'test': True,  # Activation des tests automatiques
}