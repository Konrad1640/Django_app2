# restauracja/forms.py
from django import forms
from .models import Dish, Review

class DishSearchForm(forms.Form):
    query = forms.CharField(required=False, label='Szukaj dania', max_length=100)

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'image']  # Pola, które chcesz wyświetlić w formularzu

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['dish', 'rating', 'comment']

    # Optional field for user to add a comment (max length can be set as desired)
    comment = forms.CharField(widget=forms.Textarea, required=False, label="Komentarz")
    rating = forms.ChoiceField(choices=[(i, f'{i} gwiazdek') for i in range(1, 6)], label="Ocena")