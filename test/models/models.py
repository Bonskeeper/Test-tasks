# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class test(models.Model):
    _name = 'test.test'


    name = fields.Char(string="Test name", required=True)
    test_purpose = fields.Text()
    tester = fields.Many2one('res.partner', string="Tester")


class test_session(models.Model):
    _name = 'test.test_session'
    
    name = fields.Char(string="Test session name", required=True)
    test = fields.Reference([('test.test', 'Test Name')])
    start_date = fields.Date()
    end_date = fields.Date()
    duration = fields.Integer(string="Duration in day(s)", compute="_value_duration", store=True)

    @api.depends('end_date')
    def _value_duration(self):
	fmt = '%Y-%m-%d'
	if self.start_date and self.end_date:
		d1 = datetime.strptime(self.start_date, fmt)
		d2 = datetime.strptime(self.end_date, fmt)
        	self.duration = str((d2-d1).days)


# class test(models.Model):
#     _name = 'test.test'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
