{
    'name':'client',
    'author':'ulrich',
    'website':'odoo.tech',
    'sumary':'odoo16 Development',
    'depends':['purchase','product',''],
    'data':[
        'views/client.xml',  
       
    ],
    'development_status': 'alpha',
    'application': True,
    
    'installable': True,
     'test': True,  # Activation des tests automatiques
}