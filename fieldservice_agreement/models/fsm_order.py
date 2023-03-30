# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class FSMOrder(models.Model):
    _inherit = "fsm.order"

    agreement_id = fields.Many2one("agreement", string="Agreement")
    serviceprofile_id = fields.Many2one("agreement.serviceprofile", "Service Profile")
    partner_location_id = fields.Many2one(
        "res.partner", string="Partner Location", compute="_compute_partner_location_id"
    )

    @api.depends("location_id.partner_id", "location_id.partner_id.parent_id")
    def _compute_partner_location_id(self):
        for order in self:
            if order.location_id.owner_id.parent_id:
                order.partner_location_id = order.location_id.owner_id.parent_id
            else:
                order.partner_location_id = order.location_id.owner_id
