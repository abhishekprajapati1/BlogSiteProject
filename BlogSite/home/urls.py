from django.urls import  path, include
from . import views


# creating my home urlconf.

urlpatterns = [
    path('', include('articles.urls')),

]