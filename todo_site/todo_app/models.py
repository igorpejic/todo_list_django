from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from cities.models import Country, City

from .weather_utils import get_color_from_weather, get_weather_data


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    is_done = models.BooleanField(default=False)

    latitude = models.FloatField()
    longitude = models.FloatField()

    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    saved_temperature = models.FloatField(null=True, blank=True)
    saved_weather = models.CharField(max_length=40, null=True, blank=True)

    @property
    def temperature(self):
        if self.is_done and self.saved_temperature:
            return self.saved_temperature
        _, temperature = get_weather_data(self.longitude, self.latitude)
        return temperature

    @property
    def weather(self):
        if self.is_done and self.saved_weather:
            return self.saved_weather
        weather, _ = get_weather_data(self.longitude, self.latitude)
        return weather

    @property
    def weather_color(self):
        return get_color_from_weather(self.weather)

    def save(self, *args, **kwargs):
        if self.pk:
            original_todo = Todo.objects.get(pk=self.pk)
            if self.is_done != original_todo.is_done:
                # 'is_done' has changed, save 'saved_temperature' and 'saved_weather' recorded at the time of saving.
                if self.is_done:
                    self.saved_temperature, self.saved_weather = (
                        self.temperature,
                        self.weather,
                    )
                else:
                    # Otherwise reset the fields.
                    self.saved_temperature, self.saved_weather = None, None

        super(Todo, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Todo(title='{self.title}', is_done={self.is_done}')"

    class Meta:
        ordering = ("modified_at",)
