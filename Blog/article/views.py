from django.shortcuts import render, HttpResponse

# Create your views here.

def bloghome(request):
    return render(request, 'article/home.html')
    # return HttpResponse("This is blog page we will keep all the blog post here")


def blogpost(request, slug):
    return render(request, 'article/post.html')
    return HttpResponse(f"This is blogpost page for {slug}")