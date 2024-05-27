from django.shortcuts import render
from django.http import HttpResponse
from .models import Thing, Review

def home(request):
    return render(request, 'main/home.html')


def menu(request):
    things = Thing.objects.all()
    return render(request, 'main/menu.html', {'things': things})

def reviews(request): 
    reviews = Review.objects.all()
    return render(request, 'main/reviews.html', {'reviews': reviews})


def contact(request):
    return render(request, 'main/contact.html')
