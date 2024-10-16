# Copyright 2022 Rafnix Guzman
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Fieldservice Equipment Labels and Qrcode",
    "summary": """
        This module is an add-on for the Field Service application in Odoo.
        It allows you go to your FSM Equipments print
        Labels and QRcode with URL to fieldserice_equipment_website.""",
    "version": "14.0.1.0.2",
    "license": "AGPL-3",
    "website": "https://github.com/OCA/field-service",
    "author": "Odoo Community Association (OCA), Rafnix Guzman",
    "depends": ["fieldservice_equipment_website"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_company_views.xml",
        "views/fsm_equipment_views.xml",
        "views/fsm_calibration_certificate_views.xml",
        "reports/fieldservice_equipment_report.xml",
        "reports/fieldservice_equipment_report_template.xml",
    ],
    "demo": [],
}
