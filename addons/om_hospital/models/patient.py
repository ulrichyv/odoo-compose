# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit =  'mail.thread'
    name = fields.Char(string='Name', required=True,tracking=True)
    age=fields.Integer(string="age",tracking=True)
    is_child=fields.Boolean(string="is_child?",tracking=True)
    notes=fields.Text(string="Notes")
    gender=fields.Selection([("male","Male"),("female","Female")],string="Gender",tracking=True)
     
    Capitalized_name=fields.Char(string='Capitalized Name', compute='_compute_capitalized_name')
    
    def _compute_capitalized_name(self):
        self.Capitalized_name='TEST'


    @api.onchange('age')
    def  onchange_age (self):
        if self.age <=10:
            self.is_child=True
        else:
            self.is_child=False    
       