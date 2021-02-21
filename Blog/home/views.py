from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home/home.html')
    # return HttpResponse("This is home page")

def contact(request):
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')