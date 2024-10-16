# -*- coding: utf-8 -*-
# from odoo import http


# class CustomBooleanStyle(http.Controller):
#     @http.route('/custom_boolean_style/custom_boolean_style', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_boolean_style/custom_boolean_style/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_boolean_style.listing', {
#             'root': '/custom_boolean_style/custom_boolean_style',
#             'objects': http.request.env['custom_boolean_style.custom_boolean_style'].search([]),
#         })

#     @http.route('/custom_boolean_style/custom_boolean_style/objects/<model("custom_boolean_style.custom_boolean_style"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_boolean_style.object', {
#             'object': obj
#         })
