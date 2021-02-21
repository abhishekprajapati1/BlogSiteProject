from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This is home page")

def contact(request):
    return HttpResponse("This is contact page")

def about(request):
    return HttpResponse("This is about page")