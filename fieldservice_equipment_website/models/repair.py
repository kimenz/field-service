from odoo import api, fields, models


class RepairOrder(models.Model):
    _inherit = "repair.order"

    equipment_id = fields.Many2one(
        "fsm.equipment",
        string="Equipment",
        domain="[('product_id', '=', product_id)]",
        help="Equipment used for this repair",
    )

    @api.onchange("product_id")
    def _onchange_product_id(self):
        if self.product_id:
            self.equipment_id = self.env["fsm.equipment"].search(
                [("product_id", "=", self.product_id.id)], limit=1
            )
        else:
            self.equipment_id = False
