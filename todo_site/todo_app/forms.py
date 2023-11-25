from django import forms
from .models import Todo
from cities.models import Country, City


class TodoForm(forms.ModelForm):
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(), empty_label="Select a country"
    )
    # The queryset of possible cities is dynamically updated
    # in the fronted based on the country chosen.
    city = forms.ModelChoiceField(
        queryset=City.objects.none(), empty_label="Select a city"
    )

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        # In case of updates, if country is already set, we want to also return a valid option of cities.
        if "country" in self.data:
            try:
                country_id = int(self.data.get("country"))
                self.fields["city"].queryset = City.objects.filter(
                    country_id=country_id
                ).order_by("name")
            except (ValueError, TypeError):
                pass  # Invalid input; fallback to empty city queryset
        elif self.instance.pk:
            self.fields["city"].queryset = self.instance.country.cities.order_by("name")

    def save(self, commit=True):
        instance = super().save(commit=False)
        city = self.cleaned_data["city"]
        country = self.cleaned_data["country"]
        if city:
            instance.city = city
            instance.country = country
            instance.longitude = city.location[0]
            instance.latitude = city.location[1]
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Todo
        fields = ["title", "country", "city"]
