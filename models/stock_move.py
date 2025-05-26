from odoo import models, fields

class StockMove(models.Model):
    _inherit = 'stock.move'
    
    picking_partner_id = fields.Many2one(
        'res.partner',
        string="Contacto de Transferencia",
        related='picking_id.partner_id',
        store=True,
        readonly=True
    )