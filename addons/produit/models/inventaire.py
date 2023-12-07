from odoo import fields, models

class Inventaire(models.Model):
   _inherit = 'product.template'
   date_de_reception = fields.Date(String="Date de recepetion" , required = True)
   numero_de_lot = fields.Char(String="Numéro de Lot" , required = True)
   conditionement = fields.Char(String = "Conditionement", required=True)
   dosage = fields.Char(String = "Dosage", required=True)