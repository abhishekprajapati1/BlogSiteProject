from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def bloghome(request):
    allPosts = Post.objects.all()
    context = {
        'allPosts':allPosts,
    }
    return render(request, 'article/home.html', context)

def blogpost(request, slug):
    return render(request, 'article/post.html')