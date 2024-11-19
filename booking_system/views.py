from django.shortcuts import render
from django.forms import Bookingform

def home(request):
    return render(request, 'devconnect/home.html')

def booking_view(request):
    return render(request, 'devconnect/booking.html')

def about(request):
    return render(request, 'devconnect/about.html')


def booking_view(request):
    if request.method == "POST":
        form = bookingform(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('booking_success')
    else:
        form = bookingform()
    
    return render (request, 'devconnect/booking.html', {'form': form})

