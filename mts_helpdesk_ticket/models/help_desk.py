# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HelpDesk(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Help Desk Ticket'

    # Fields of models ticket
    name = fields.Char(string="Ticket Name", required=True)
    client_id = fields.Many2one('res.partner', string="Client Name")
    state = fields.Selection([
        ('new','New'),
        ('in_progress','In progress'),
        ('done','Done')], string="State", default='new')
    description = fields.Html(string="Description")
    create_date = fields.Datetime(string="Creation Date", default=lambda self: fields.Datetime.now())
    user_assigned_id = fields.Many2one('res.users', string="User Assigned")


