# urls.py

from django.urls import path
from .views import validate_policy

urlpatterns = [
    path('validate_policy/', validate_policy, name='validate_policy'),
]