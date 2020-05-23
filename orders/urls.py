# orders/urls.py
from django.urls import path

from .views import OrderPageView, charge

urlpatterns = [
    # Django admin
    path('charge/', charge, name='charge'),
    path('', OrderPageView.as_view(), name='orders'),
]

