# Copyright (C) 2018 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models


class FSMWizard(models.TransientModel):
    _inherit = "fsm.wizard"

    def _prepare_fsm_location(self, partner):
        res = super()._prepare_fsm_location(partner)
        partner = partner.parent_id or partner
        res["customer_id"] = partner.id
        res["owner_id"] = partner.id
        return res
