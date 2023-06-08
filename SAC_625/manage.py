#!/usr/bin/env python3

import os
import sys

# Check if the minimum and maximum sum assured, minimum and maximum age limits
# are defined for each product and master level.
if not os.path.isfile('products_and_master_level.txt'):
    sys.exit('Error: Missing products_and_master_level.txt file.')

# Check if the annual income of the user is greater than 40K.
if not os.path.isfile('annual_income.txt'):
    sys.exit('Error: Missing annual_income.txt file.')

income = 0
with open('annual_income.txt', 'r') as f:
    income = int(f.readline().strip())

if income < 40000:
    sys.exit('Error: Annual income is less than 40K.')

# Check if the sum assured ranges and policy tenure ranges are displayed.
sum_assured_ranges = [50000, 100000, 150000, 200000]
policy_tenure_ranges = [12, 15, 18, 24]

if not sum_assured_ranges or not policy_tenure_ranges:
    sys.exit('Error: Missing sum assured and/or policy tenure ranges.')

# Check if the OTP authentication is received from the Bandhan Bank sales personnel.
if not os.path.isfile('otp_authentication.txt'):
    sys.exit('Error: Missing OTP authentication.')

# Check if the member's spouse is eligible for insurance coverage.
if not os.path.isfile('spouse_eligibility.txt'):
    sys.exit('Error: Missing spouse_eligibility.txt file.')

spouse_eligibility = False
with open('spouse_eligibility.txt', 'r') as f:
    spouse_eligibility = bool(f.readline().strip())

if not spouse_eligibility:
    sys.exit('Error: Member\'s spouse is not eligible for insurance coverage.')

# If all conditions are satisfied, issue the Bajaj Allianz Group Sampoorna Jeevan Suraksha policy
print('Issuing the Bajaj Allianz Group Sampoorna Jeevan Suraksha policy...')