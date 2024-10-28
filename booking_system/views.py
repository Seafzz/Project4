from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return HttpResponse("WElcome to the booking System!")
