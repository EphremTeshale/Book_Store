from django.urls import path

from .views import SignUpPageView


urlpatterns = [
    # Signup
    path('signup/', SignUpPageView.as_view(),name='signup'),
]