# -*- coding: utf-8 -*-

from odoo import models, fields, api

class products(models.Model):
     _name = 'furn.products'

     name = fields.Selection([('b', 'Bed Room'), ('c', 'Child Room') , ('l', 'Living Room'), ('d', 'Dinning Room') ,
                               ('k', 'kitchen'), ('s', 'Salon')])
     type = fields.Char(string="Type")
     no_of_pieces = fields.Integer(string="Number Of Pieces")
     name_of_designer = fields.Char(string="Name Of Designer", required=True)
     color = fields.Selection([('r', 'Red'), ('b', 'Blue') , ('y', 'Yellow'), ('g', 'Green') ,
                               ('p', 'Pink'), ('v', 'Violet') , ('w', 'White'), ('bl', 'Black')])
     product_code = fields.Integer(string="Product Code")
     price = fields.Float(string="Price" , required=True)
     note = fields.Text()

     #@api.depends('value')
     #def _value_pc(self):
        # self.value2 = float(self.value) / 100