from django import forms
from .models import Todo
from cities.models import Country, City


class TodoForm(forms.ModelForm):
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(), empty_label="Select a country"
    )
    city = forms.ModelChoiceField(
        queryset=City.objects.none(), empty_label="Select a city"
    )

    class Meta:
        model = Todo
        fields = ["title", "location"]
