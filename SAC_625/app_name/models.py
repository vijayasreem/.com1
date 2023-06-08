class BajajAllianzGroupSampoornaJeevanSurakshaPolicy:
    def __init__(self):
        self.min_sum_assured = None
        self.max_sum_assured = None
        self.min_age_limit = None
        self.max_age_limit = None
        self.annual_income_limit = 40000
        self.sum_assured_ranges = [50000, 100000, 150000, 200000]
        self.policy_tenure_ranges = [12, 15, 18, 24]
        self.spouse_eligibility = False
        self.otp_authentication = False
    
    def validate_policy(self, min_sum_assured, max_sum_assured, min_age_limit, max_age_limit, annual_income, policy_tenure):
        if min_sum_assured < self.min_sum_assured or max_sum_assured > self.max_sum_assured:
            raise ValueError('Sum assured range is not valid')
        if min_age_limit < self.min_age_limit or max_age_limit > self.max_age_limit:
            raise ValueError('Age limit is not valid')
        if annual_income < self.annual_income_limit:
            raise ValueError('Annual income is not valid')
        if policy_tenure not in self.policy_tenure_ranges:
            raise ValueError('Policy tenure is not valid')
        if self.spouse_eligibility and not self.otp_authentication:
            raise ValueError('OTP authentication is not valid')
        return True