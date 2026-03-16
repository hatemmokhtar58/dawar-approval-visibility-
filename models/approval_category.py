from odoo import models, fields

class ApprovalCategory(models.Model):
    _inherit = 'approval.category'

    allowed_group_ids = fields.Many2many(
        'res.groups', 
        string='المجموعات المسموح لها بالرؤية',
        help='إذا تم تركه فارغاً، سيظهر الطلب للجميع. وإذا تم تحديد مجموعات، سيظهر فقط لمستخدمي هذه المجموعات.'
    )
