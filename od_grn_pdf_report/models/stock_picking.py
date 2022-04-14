from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def get_purchase_number(self):
        po_date = self.move_ids_without_package[0].purchase_line_id.order_id.date_approve
        return po_date

    def get_invoice_number(self):
        invoice_num = '/'
        if self.picking_type_code == 'incoming':
            if self.move_ids_without_package:
                if self.move_ids_without_package[0].purchase_line_id.invoice_lines:
                    invoice_num = self.move_ids_without_package[0].purchase_line_id.invoice_lines[0].move_id.name
        else:
            invoice_num = self.sale_id.name or '/'
        return invoice_num
