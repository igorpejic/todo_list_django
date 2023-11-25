from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    is_done = models.BooleanField(default=False)
    location = models.CharField(max_length=400)

    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Todo(title='{self.title}', is_done={self.is_done}, location='{self.location}')"

    class Meta:
        ordering = ("modified_at",)
