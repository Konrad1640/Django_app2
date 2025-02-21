from django.shortcuts import redirect, render, get_object_or_404
from .models import Dish, Reservation, Review
from .forms import DishSearchForm, DishForm, ReviewForm
from django.urls import reverse
from django.contrib import messages

def user_menu(request):
    dishes = Dish.objects.all()
    return render(request, 'user_menu.html', {'dishes': dishes})


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

def reviews_view(request):
    reviews = Review.objects.select_related('user', 'dish').all()  # Fetch all reviews with related data
    star_range = range(1, 6)  # Generate a range from 1 to 5

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Save the form and associate the review with the current user
            review = form.save(commit=False)
            if request.user.is_authenticated:  # If the user is authenticated, assign the review to them
                review.user = request.user
            else:
                review.user = None  # If not authenticated, assign a default value (e.g., Anonymous or None)
                messages.error(request, 'Musisz być zalogowany, aby dodać opinię.')  # Inform about login requirement
            
            review.save()
            messages.success(request, 'Dziękujemy za dodanie opinii!')  # Add success message
            return redirect('reviews')  # Redirect to the same page after successful submission
    else:
        form = ReviewForm()

    return render(request, 'reviews.html', {'reviews': reviews, 'form': form, 'star_range': star_range})


