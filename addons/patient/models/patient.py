# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError

import datetime

class Patient(models.Model):
    _name = "patient"
    _inherit = 'mail.thread'

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender", tracking=True)
    # Additional fields
    address = fields.Char(string="Address")
    phone_number = fields.Char(string="Phone Number")
    email = fields.Char(string="Email")
    allergies = fields.Text(string="Allergies")
    medicaments = fields.Text(string="Medicaments")
    reminder_value = fields.Integer(string="le nombre de temps")
    reminder_unit = fields.Selection([
        ('days', 'Days'),
        ('weeks', 'Weeks'),
        ('months', 'Months')
    ], string="periode")
    frequency = fields.Integer(string="nombre de frequence ")
    @api.constrains('email')
    def _check_email(self):
        for patient in self:
            if patient.email and not self._is_valid_email(patient.email):
                raise ValidationError("Invalid email format.")

    def _is_valid_email(self, email):
        # Ajoutez ici votre logique de validation de l'e-mail
        # Par exemple, vous pouvez utiliser des expressions régulières
        # ou des bibliothèques de validation d'e-mail
        # Retournez True si l'e-mail est valide, False sinon
        return True  # Modifier selon vos besoins

    @api.constrains('reminder_value')
    def _check_reminder_value(self):
        for patient in self:
            if patient.reminder_value <= 0:
                raise ValidationError("Reminder value must be a positive number.")
            
    @api.onchange('medicaments', 'reminder_value', 'reminder_unit', 'frequency')
    def send_mail(self):
        if self.medicaments and self.reminder_value and self.reminder_unit and self.frequency:
            current_time = datetime.datetime.now()
            #transformation  du nombre de temps pour prendre le medicament  en date en fonction de la periode
            if self.reminder_unit == 'days':
                reminder_duration = datetime.timedelta(days=self.reminder_value)
            elif self.reminder_unit == 'weeks':
                reminder_duration = datetime.timedelta(weeks=self.reminder_value)
            elif self.reminder_unit == 'months':
                reminder_duration = datetime.timedelta(months=self.reminder_value)
            reminder_time = current_time + reminder_duration
            frequence = self.frequency
            # recuperation du nombre de fois qu'il doit prendre le medicament 
            for i in range(frequence):
                reminder_time = reminder_time + reminder_duration
                
                message = self.env['mail.message'].create({
                     'subject': 'Médicaments à prendre',
                     'body': '<p>Vous devez prendre les médicaments </p>',
                      'date': reminder_time,
                     })
               # message.send()

 
              
    
    
    
  

       