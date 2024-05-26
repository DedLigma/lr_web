from django.shortcuts import render
from .models import Pelmeni, BlogPost

def home(request):
    return render(request, 'main/home.html')

from django.http import HttpResponse
from .models import Pelmeni, BlogPost

def menu(request):
    pelmenis = Pelmeni.objects.all()
    for pelmeni in pelmenis:
        print(pelmeni.name)  
    return render(request, 'main/menu.html', {'pelmenis': pelmenis})

def blog(request):
    blog_posts = BlogPost.objects.all()
    for post in blog_posts:
        print(post.title) 
    return render(request, 'main/blog.html', {'blog_posts': blog_posts})

def contact(request):
    return render(request, 'main/contact.html')
