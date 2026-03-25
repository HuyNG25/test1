from odoo import models, fields

class NhanVien(models.Model):
    _inherit = 'nhan_vien'

    van_ban_den_ids = fields.One2many('van_ban_den', 'nguoi_xu_ly_id', string="Văn bản đến xử lý")
    van_ban_di_ids = fields.One2many('van_ban_di', 'nguoi_gui_id', string="Văn bản đi gửi")
