from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home/home.html')
    # return HttpResponse("This is home page")

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['desc']
        print(name,email,phone,msg)

        if len(name) < 2 or len(email) < 5 or len(phone) < 10 or len(msg) < 5:
            messages.error(request, 'Please fill the form correctly')
        else:
            contact = Contact(name=name, phone=phone, email=email, content=msg)
            contact.save()
            messages.success(request, 'Sent successfully')
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')