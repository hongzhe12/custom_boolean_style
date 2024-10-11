# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_boolean_style(models.Model):
    _name = 'custom_boolean_style.custom_boolean_style'
    _description = 'custom_boolean_style.custom_boolean_style'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    is_active = fields.Boolean(string='是否活跃')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
