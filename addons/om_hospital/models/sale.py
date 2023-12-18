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
        
        return {
            'type': 'ir.actions.act_window',
            'name': 'Recommended Products',
            'res_model': 'product.product',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', [p.id for p in produits_alternatifs])],
        }


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def alternative(self):
        stock_quant = self.env['stock.quant'].search([('product_id', '=', self.product_id.id)])
        if stock_quant:
            return False
        else:
            produit = self.env['product.product'].search([('dci', '=', self.product_id.dci)])
            if produit:
                return produit
            else:
                return False