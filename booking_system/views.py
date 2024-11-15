from django.shortcuts import render

def home(request):
    return render(request, 'devconnect/home.html')

def booking_view(request):
    return render(request, 'devconnect/booking.html')

def about(request):
    return render(request, 'devconnect/about.html')

def about (request):
    return render (request, 'devconnect/booking_sucess.html')
