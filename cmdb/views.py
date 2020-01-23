from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello 4X!!")

def emotion(request):
    return  render(request, 'frame.html')