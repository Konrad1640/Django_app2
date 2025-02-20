# restauracja/forms.py
from django import forms
from .models import Dish

class DishSearchForm(forms.Form):
    query = forms.CharField(required=False, label='Szukaj dania', max_length=100)

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'image']  # Pola, które chcesz wyświetlić w formularzu
