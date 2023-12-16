# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_description = fields.Char(string='Sale Description')
    order_line_ids = fields.One2many('sale.order.line', 'order_id', string="Produits")

    def action_alter(self):
        produits_alternatifs = []
        for order_line in self.order_line_ids:
            produit = order_line.alternative()
            if produit:
                produits_alternatifs.append(produit)
        if produits_alternatifs:
            return produits_alternatifs
        else:
            return "Aucun produit alternatif trouvé"


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def alternative(self):
        produit = self.env['product.template'].search([('dci', '=', self.product_id.dci)])
        if produit:
            return produit
        else:
            return False