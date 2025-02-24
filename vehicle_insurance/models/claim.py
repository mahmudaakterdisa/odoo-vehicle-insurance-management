from odoo import models, fields

class InsuranceClaim(models.Model):
    _name = 'insurance.claim'
    _description = 'Insurance Claim'

    claim_number = fields.Char(string="Claim Number", required=True, copy=False, readonly=True, default='New')
    policy_id = fields.Many2one('insurance.policy', string="Policy", required=True)

    claim_purpose = fields.Selection([
        ('none', 'Select Claim Purpose'),
        ('damage', 'Damage'),
        ('accident', 'Accident'),
        ('theft', 'Theft'),
        ('fire', 'Fire'),
        ('total_loss', 'Total Loss')
    ], string="Claim Purpose", required=True, default='none')

    claim_date = fields.Date(string="Claim Date", required=True)
    claim_amount = fields.Float(string="Claim Amount", required=True)

    status = fields.Selection([
        ('none', 'Select Status'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string="Status", required=True, default='none')

