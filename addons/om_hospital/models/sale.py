# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_description = fields.Char(string='Sale Description')
    
    
    
class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def alternative(self):
        produit = self.env['product.template'].search([('dci', '=', self.product_id.dci)])
        if produit:
            return  produit
        else:
            return False
        
  


