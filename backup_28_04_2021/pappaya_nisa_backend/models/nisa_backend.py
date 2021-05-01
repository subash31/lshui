# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import except_orm, ValidationError
import re
from datetime import datetime


invalid_mobile_numbers = ['0000000000', '1111111111', '2222222222', '3333333333', '4444444444',
                          '5555555555', '6666666666',
                          '7777777777', '8888888888', '9999999999']

class pappaya_nisa_backend(models.Model):
    _name = 'pappaya.nisa.backend'
    _description = "Nisa Backend Model"

    name = fields.Char('Name')
    first_name = fields.Char('First Name')
    last_name = fields.Char('Last Name')
    user_email = fields.Char('User Email')
    user_mobile = fields.Char('User Mobile', size=10)
    school_name = fields.Char('School Name')
    district = fields.Many2one('state.district', 'District')
    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    zip = fields.Char('Zip', size=6)
    city = fields.Char('City')
    state_id = fields.Many2one('res.country.state', string="State", domain=[('country_id.is_active', '=', True)])
    country_id = fields.Many2one('res.country', string="Country", default=105)
    status = fields.Selection([('requested','Requested'),('created', 'Created')])



    # @api.multi
    def unlink(self):
        raise ValidationError('Sorry,You are not authorized to delete record')

    # @api.one
    def copy(self, default=None):
        raise ValidationError("You are not allowed to Duplicate")
