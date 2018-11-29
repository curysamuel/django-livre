from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=200)
    participantes = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='autor')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event_edit', kwargs={'pk': self.pk})
