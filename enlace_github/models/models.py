# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EnlaceGithub(models.Model):
    _inherit = 'res.partner'

    enlace = fields.Char("EnlaceGit")
