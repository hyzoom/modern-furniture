# -*- coding: utf-8 -*-

from odoo import models, fields, api


class employees(models.Model):
    _name = 'furn.employees'

    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address")
    phon_no = fields.Integer(string="Phone Number")
    gender = fields.Selection([('m', 'Male'), ('f', 'Female')])
    age = fields.Float()
    note = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    # self.value2 = float(self.value) / 100


class mangers(models.Model):
    _name = 'furn.mangers'
    _inherit = 'furn.employees'

    nmb_experience = fields.Char(string="Number of experience")


class designers(models.Model):
    _name = 'furn.designers'
    _inherit = 'furn.employees'

    nmb_designs = fields.Char(string="Number of Designs")
