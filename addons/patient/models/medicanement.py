from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError
import datetime

class Medicament(models.Model):
    _name = "medicament"
    name = fields.Char(string='Name', required=True, tracking=True)
    quatity= fields.Integer(string="Age", tracking=True)
    