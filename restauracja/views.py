from django.shortcuts import redirect, render, get_object_or_404
from .models import Dish, Reservation, Review
from .forms import DishSearchForm, DishForm
from django.urls import reverse

def delete_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    if request.method == "POST":
        dish.delete()
        return redirect(reverse('menu'))
    return render(request, 'delete_dish_confirm.html', {'dish': dish})

def home(request):
    return render(request, 'home.html')

def menu(request):
    form = DishSearchForm(request.GET)  # Formularz oparty na zapytaniu GET
    dishes = Dish.objects.all()  # Początkowo pobieramy wszystkie dania
    
    # Jeśli formularz jest poprawny, wykonujemy filtrację
    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            # Filtrujemy dania po nazwie (ignorując wielkość liter)
            dishes = dishes.filter(name__icontains=query)

    return render(request, 'menu.html', {'dishes': dishes, 'form': form})

def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)  # Pobieramy dane z formularza
        if form.is_valid():
            form.save()  # Zapisujemy dane do bazy
            return redirect('menu')  # Przekierowujemy na stronę menu po zapisaniu
    else:
        form = DishForm()  # Jeżeli formularz jest pusty, to go wyświetlamy
    
    return render(request, 'add_dish.html', {'form': form})


def reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations.html', {'reservations': reservations})

def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})

