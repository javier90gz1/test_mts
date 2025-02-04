# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HelpDesk(models.Model):
    _name = 'helpdesk.ticket'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _mail_post_access = 'read'
    _description = 'Help Desk Ticket'

    # Fields of models helpdesk.ticket
    name = fields.Char(string="Ticket Name", required=True, tracking=True)
    client_id = fields.Many2one('res.partner', string="Client Name", tracking=True)
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In progress'),
        ('done', 'Done')], string="State", default='new', tracking=True)
    description = fields.Html(string="Description", tracking=True)
    create_date = fields.Datetime(string="Creation Date", default=lambda self: fields.Datetime.now())
    user_assigned_id = fields.Many2one('res.users', string="User Assigned", tracking=True)

    # method to change state to 'done'
    def action_check_done(self):
        self.state = 'done'

    # method to change state to 'progress'
    def action_check_in_progress(self):
        self.state = 'in_progress'
