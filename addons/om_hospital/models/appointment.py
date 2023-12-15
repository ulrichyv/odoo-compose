# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import datetime
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _order = "doctor_id,name,age"

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                       default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    age = fields.Integer(string='Age', related='patient_id.age', tracking=True, store=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor", required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string="Gender")
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')], default='draft',
                             string="Status", tracking=True)
    note = fields.Text(string='Description')
    date_appointment = fields.Date(string="Date")
    date_checkup = fields.Datetime(string="Check Up Time")
    prescription = fields.Text(string="Prescription")
    prescription_line_ids = fields.One2many('appointment.prescription.lines', 'appointment_id',
                                            string="Prescription Lines")
    medicament_line_ids = fields.One2many('appointment.medicament.lines', 'appointment_id',
                                            string="medicament lines")
    def action_rende_vous(self):
      for medicament_line in self.medicament_line_ids:
           medicament_line.rende_vous()
      
    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        res = super(HospitalAppointment, self).create(vals)
        return res

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        if self.patient_id:
            if self.patient_id.gender:
                self.gender = self.patient_id.gender
            if self.patient_id.note:
                self.note = self.patient_id.note
        else:
            self.gender = ''
            self.note = ''

    def unlink(self):
        if self.state == 'done':
            raise ValidationError(_("You Cannot Delete %s as it is in Done State" % self.name))
        return super(HospitalAppointment, self).unlink()

   


class AppointmentPrescriptionLines(models.Model):
    _name = "appointment.prescription.lines"
    _description = "Appointment Prescription Lines"

    name = fields.Char(string="Medicine", required=True)
    qty = fields.Integer(string="Quantity")
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
    
class AppointmentMedicament(models.Model):
    _name = "appointment.medicament.lines"
    _description = "Appointment Medicament"

    product_id = fields.Many2one('product.template', string="medicament", required=True)
    qty = fields.Integer(string="Quantity")
    reminder_value = fields.Integer(string="temps")
    reminder_unit = fields.Selection([
        ('days', 'Days'),
        ('weeks', 'Weeks'),
        ('months', 'Months')
    ], string="periode")
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
    frequency = fields.Integer(string="Frequence")
    def verifier(self):
         produit = self.env['product.template'].search([('display_name', '=', self.medicaments)])
         if produit:
           return True
         else:
          return False
        
    
    def rende_vous(self):
      if self.product_id and self.reminder_value and self.reminder_unit and self.frequency:
        current_time = datetime.datetime.now()

        if self.reminder_unit == 'days':
            reminder_duration = datetime.timedelta(days=self.reminder_value)
        elif self.reminder_unit == 'weeks':
            reminder_duration = datetime.timedelta(weeks=self.reminder_value)
        elif self.reminder_unit == 'months':
            reminder_duration = datetime.timedelta(days=self.reminder_value * 30)

        reminder_time = current_time
        frequence = self.frequency

        for i in range(frequence):
            reminder_time += reminder_duration

            message = self.env['mail.message'].create({
                'subject': 'Médicaments à prendre',
                'body': '<p>Vous devez prendre les médicaments : {}</p>'.format(self.product_id.name),
                'date': reminder_time,
            })

            calendar = self.env['calendar.event'].create({
                'name': 'Patient: ' + self.appointment_id.patient_id.name,
                'description': 'Prescription: ' + self.product_id.name,
                'start': reminder_time,
                'stop': reminder_time + datetime.timedelta(hours=2),
            })
       
   

