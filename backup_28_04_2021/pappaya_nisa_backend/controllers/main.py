from odoo import http
from odoo.http import request
from werkzeug import utils
import requests
import json
import base64


class Nisauserregistration(http.Controller):

    @http.route('/lifespace/registration', website=True, type='http', auth='public')
    def registration_portal(self, **kw):
        return request.render('pappaya_nisa_backend.nisa_home_page',)

    @http.route('/lifespace/designs', website=True, type='http', auth='public')
    def reg1(self, **post):
        return request.render('pappaya_nisa_backend.nisa_styles',)

    @http.route('/lifespace/industrial', website=True, type='http', auth='public')
    def reg2(self, **post):
        return request.render('pappaya_nisa_backend.nisa_industrial',)

    @http.route('/lifespace/minimal', website=True, type='http', auth='public')
    def reg3(self, **post):
        return request.render('pappaya_nisa_backend.nisa_minimal',)
        
    @http.route('/lifespace/pop', website=True, type='http', auth='public')
    def reg4(self, **post):
        return request.render('pappaya_nisa_backend.nisa_pop',)


    @http.route('/lifespace/urbanluxury', website=True, type='http', auth='public')
    def reg5(self, **post):
        return request.render('pappaya_nisa_backend.nisa_urban',)

    @http.route('/lifespace/wishlist', website=True, type='http', auth='public')
    def reg6(self, **post):
        return request.render('pappaya_nisa_backend.nisa_wishlist',)   

    @http.route('/lifespace/productdetail', website=True, type='http', auth='public')
    def reg7(self, **post):
        return request.render('pappaya_nisa_backend.lsh_prod_detail',)      

        
