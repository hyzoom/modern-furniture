# -*- coding: utf-8 -*-

from odoo import models, fields, api

class manufactory(models.Model):
     _name = 'furn.manufactory'

     address = fields.Char(string="Address" , required= True)
     no_of_worker = fields.Integer(string="Number Of Worker" , required= True)
     no_of_products = fields.Integer(string="Number Of Products")
     note = fields.Text()

     #@api.depends('value')
     #def _value_pc(self):
        # self.value2 = float(self.value) / 100