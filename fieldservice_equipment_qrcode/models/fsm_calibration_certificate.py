from odoo import fields, models


class FsmCalibrationCertificate(models.Model):

    _name = "fsm.calibration.certificate"
    _description = "Calibration Certificate"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Name", required="True", tracking=True)
    initial_date = fields.Date(string="Initial Date", tracking=True)
    expiration_date = fields.Date(string="Expiration Date", tracking=True)
    notes = fields.Text(string="Notes")
    fsm_equipment_id = fields.Many2one(
        "fsm.equipment", string="Equipment", tracking=True
    )
    certificate_file = fields.Binary(
        string="Certificate File", tracking=True, attachment=True
    )
    active = fields.Boolean(string="Active", default=True, tracking=True)
