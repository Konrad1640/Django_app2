from django.shortcuts import render
from .models import Dish, Reservation, Review

def home(request):
    return render(request, 'home.html')

def menu(request):
    dishes = Dish.objects.all()
    return render(request, 'menu.html', {'dishes': dishes})

def reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations.html', {'reservations': reservations})

def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})
