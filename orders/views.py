# orders/views.py

from django.views.generic.base import TemplateView


class OrderPageView(TemplateView):
    template_name = "orders/purchase.html"
