from odoo import fields, models


class Commande(models.Model):
    _inherit = 'purchase.order'

    region = fields.Selection([
        ("littoral", "LITTORAL"),
        ("centre", "CENTRE"),
        ("extrême-Nord", "Extrême-Nord")
    ], string="Region", tracking=True)

    aire_de_Sante = fields.Char(string="aire de santé")
    structure = fields.Char(string="structure")
    BC = fields.Char(string="N° BC")
    
    
   
    
    
    
