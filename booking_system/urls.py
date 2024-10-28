from django.urls import path
from .views import home, booking_view, about

urlpatterns = [
    path('', home, name='home'),
    path('booking/', booking_view, name='booking'),
    path('about/', about, name='about'),
]