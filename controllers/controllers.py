# -*- coding: utf-8 -*-
from odoo import http

# class ModernFurn(http.Controller):
#     @http.route('/modern_furn/modern_furn/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modern_furn/modern_furn/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modern_furn.listing', {
#             'root': '/modern_furn/modern_furn',
#             'objects': http.request.env['modern_furn.modern_furn'].search([]),
#         })

#     @http.route('/modern_furn/modern_furn/objects/<model("modern_furn.modern_furn"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modern_furn.object', {
#             'object': obj
#         })