from odoo import models, fields, api

class InsuranceCustomer(models.Model):
    _name = 'insurance.customer'
    _description = 'Insurance Customer'

    name = fields.Char(string="Customer Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    address = fields.Text(string="Address")

    existing_insurance_policy_type = fields.Selection([
        ('none', 'No Policy'),  # ✅ Default empty option
        ('premium_cars', 'Premium Vehicles and Vintage Cars'),
        ('exclusive_valuables', 'Exclusive Valuables')
    ], string="Existing Insurance Policy Type", readonly=True, default='none')

    status = fields.Selection([
        ('none', 'No Policy'),  # ✅ Default empty option
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled')
    ], string="Status", readonly=True, default='none')

    def update_policy_info(self, policy):
        """Update customer's insurance policy type & status"""
        self.write({
            'existing_insurance_policy_type': policy.insurance_policy_type,
            'status': policy.status
        })