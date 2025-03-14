import json
import requests
from odoo import models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model_create_multi
    def create(self, vals_list):
        orders = super().create(vals_list)
        for order in orders:
            order.export_to_webhook()
        return orders

    def write(self, vals):
        result = super().write(vals)
        self.export_to_webhook()
        return result

    def export_to_webhook(self):
        webhook_url = 'https://webhook.site/611830a3-3b11-46b2-b162-86a2add81d60'

        headers = {'Content-Type': 'application/json'}
        for order in self:
            data = {
                'id': order.id,
                'name': order.name,
                'customer': order.partner_id.name,
                'total_amount': order.amount_total,
                'date_order': str(order.date_order),
                'state': order.state,
                'order_lines': [
                    {
                        'product': line.product_id.name,
                        'quantity': line.product_uom_qty,
                        'price_unit': line.price_unit,
                        'subtotal': line.price_subtotal,
                    } for line in order.order_line
                ]
            }

            try:
                requests.post(webhook_url, data=json.dumps(data), headers=headers, timeout=10)
            except Exception as e:
                _logger = self.env['ir.logging']
                _logger.create({
                    'name': 'Webhook Export Error',
                    'type': 'server',
                    'dbname': self._cr.dbname,
                    'level': 'ERROR',
                    'message': f'Webhook export failed: {e}',
                    'path': 'custom_export_webhook/models/sale_order.py',
                    'func': 'export_to_webhook',
                    'line': '38',
                })
