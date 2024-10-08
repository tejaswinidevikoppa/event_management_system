
# Create your models here.
# events/models.py
from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'events/dashboard.html')

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
    registration_limit = models.PositiveIntegerField(default=100)
    status = models.CharField(choices=(('open', 'Open'), ('closed', 'Closed')), default='open', max_length=10)
    
    def __str__(self):
        return self.name

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} registered for {self.event.name}'


class CustomUser(AbstractUser):
    # Add unique related_name arguments to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Change to unique related name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Change to unique related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )