from django.db import models

# Create your models here.
# events/models.py

from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} registered for {self.event.name}'
