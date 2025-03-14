# -*- coding: utf-8 -*-
# from odoo import http


# class CustomExportWebhook(http.Controller):
#     @http.route('/custom_export_webhook/custom_export_webhook', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_export_webhook/custom_export_webhook/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_export_webhook.listing', {
#             'root': '/custom_export_webhook/custom_export_webhook',
#             'objects': http.request.env['custom_export_webhook.custom_export_webhook'].search([]),
#         })

#     @http.route('/custom_export_webhook/custom_export_webhook/objects/<model("custom_export_webhook.custom_export_webhook"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_export_webhook.object', {
#             'object': obj
#         })

