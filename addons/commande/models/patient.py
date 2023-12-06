from odoo import api, fields, models, _, tools
class HPatient(models.Model):
    _name = "patient"
    _inherit ='contact.thread'
 
     