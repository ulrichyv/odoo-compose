from odoo import fields, models

from odoo import fields, models

class producttemplate(models.Model):
    _inherit = 'product.template'
    dci = fields.Char(string="DCI", required=True, tracking=True)
