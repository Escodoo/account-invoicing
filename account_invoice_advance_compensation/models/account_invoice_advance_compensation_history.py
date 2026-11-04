# Copyright 2026, Escodoo - https://www.escodoo.com.br
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountInvoiceAdvanceCompensationHistory(models.Model):
    _name = "account.invoice.advance.compensation.history"
    _description = "Invoice Advance Compensation History"
    _order = "date desc, id desc"

    move_id = fields.Many2one(
        comodel_name="account.move",
        string="Invoice",
        required=True,
        ondelete="cascade",
        index=True,
    )
    invoice_line_id = fields.Many2one(
        comodel_name="account.move.line",
        string="Invoice Line",
        required=True,
    )
    advance_line_id = fields.Many2one(
        comodel_name="account.move.line",
        string="Advance Line",
        required=True,
    )
    compensation_move_id = fields.Many2one(
        comodel_name="account.move",
        string="Compensation Move",
        required=True,
    )
    journal_id = fields.Many2one(
        comodel_name="account.journal",
        string="Compensation Journal",
        required=True,
    )
    amount = fields.Monetary(
        string="Compensated Amount",
        currency_field="currency_id",
    )
    currency_id = fields.Many2one(
        comodel_name="res.currency",
        string="Currency",
    )
    date = fields.Date(
        string="Compensation Date",
        required=True,
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        required=True,
    )
