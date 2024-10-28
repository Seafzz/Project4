from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def booking_view(request):
    return render(request, 'booking.html')

def about(request):
    return render(request, 'about.html')
