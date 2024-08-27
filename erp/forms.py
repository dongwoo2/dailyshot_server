from django import forms

class DateSearchForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget())