# orders/urls.py
from django.urls import path

from .views import OrderPageView

urlpatterns = [
    # Django admin
    path('', OrderPageView.as_view(), name='orders'),
]

