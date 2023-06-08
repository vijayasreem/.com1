# views.py

from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.decorators import login_required

@login_required
def validate_policy(request):
    # Get data from the request
    min_sum_assured = request.POST.get('min_sum_assured')
    max_sum_assured = request.POST.get('max_sum_assured')
    min_age_limit = request.POST.get('min_age_limit')
    max_age_limit = request.POST.get('max_age_limit')
    annual_income = request.POST.get('annual_income')
    sum_assured_range = request.POST.get('sum_assured_range')
    policy_tenure_range = request.POST.get('policy_tenure_range')

    # Validate the data
    if min_sum_assured and max_sum_assured and min_age_limit and max_age_limit:
        if float(min_sum_assured) < float(max_sum_assured):
            if int(min_age_limit) < int(max_age_limit):
                if float(annual_income) >= 40000:
                    if sum_assured_range in ['50K', '1lac', '1.5 lac', '2 lac']:
                        if policy_tenure_range in ['12', '15', '18', '24']:
                            # Issue the policy
                            return redirect('success')
    
    # If criteria is not met, redirect to failure page
    return redirect('failure')