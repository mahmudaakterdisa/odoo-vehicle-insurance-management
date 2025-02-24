from odoo import models, fields, api

class InsurancePolicy(models.Model):
    _name = 'insurance.policy'
    _description = 'Insurance Policy'

    policy_number = fields.Char(string="Policy Number", required=True, copy=False, readonly=True, default='New')
    customer_id = fields.Many2one('insurance.customer', string="Customer", required=True)
    insurance_policy_type = fields.Selection([
        ('premium_cars', 'Premium Vehicles and Vintage Cars'),
        ('exclusive_valuables', 'Exclusive Valuables')
    ], string="Insurance Policy Type", required=True)

    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    premium_amount = fields.Float(string="Premium Amount", required=True)

    status = fields.Selection([
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled')
    ], string="Status", default='active')

    # Automatically update customer when policy is created or updated
    @api.model
    def create(self, vals):
        policy = super(InsurancePolicy, self).create(vals)
        if policy.customer_id:
            policy.customer_id.write({
                'existing_insurance_policy_type': policy.insurance_policy_type,
                'status': policy.status
            })
        return policy

    def write(self, vals):
        res = super(InsurancePolicy, self).write(vals)
        for policy in self:
            if policy.customer_id:
                policy.customer_id.update_policy_info(policy)
        return res

