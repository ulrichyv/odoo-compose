{
    'name':'commande',
    'author':'ulrich',
    'website':'odoo.tech',
    'sumary':'odoo16 Development',
    'depends':['purchase','product'],
    'data':[
        'views/commande.xml',  
       
    ],
    'development_status': 'alpha',
    'application': True,
    
    'installable': True,
     'test': True,  # Activation des tests automatiques
}