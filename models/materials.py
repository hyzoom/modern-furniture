# -*- coding: utf-8 -*-

from odoo import models, fields, api

class materials(models.Model):
     _name = 'furn.materials'

     name = fields.Char(string="Name" , required= True)
     amount = fields.Float(string="Amount" , required= True)
     type = fields.Char(string="Type", required=True)
     note = fields.Text()

     #@api.depends('value')
     #def _value_pc(self):
        # self.value2 = float(self.value) / 100