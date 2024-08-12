from django import forms
from .models import AlcolDrinks

class AlcolDrinksForm(forms.ModelForm):
    class Meta:
        model = AlcolDrinks
        fields = '__all__'


