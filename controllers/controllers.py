# -*- coding: utf-8 -*-
# from odoo import http


# class OpenAcaed(http.Controller):
#     @http.route('/open_acaed/open_acaed/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/open_acaed/open_acaed/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('open_acaed.listing', {
#             'root': '/open_acaed/open_acaed',
#             'objects': http.request.env['open_acaed.open_acaed'].search([]),
#         })

#     @http.route('/open_acaed/open_acaed/objects/<model("open_acaed.open_acaed"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('open_acaed.object', {
#             'object': obj
#         })
