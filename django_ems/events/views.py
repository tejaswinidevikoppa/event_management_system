from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Registration
from .forms import EventForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def event_list(request):
    events = Event.objects.all()
    print("Attempting to load template: events/event_list.html")
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user != event.organizer:
        return redirect('event_list')  # redirect if not authorized
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user == event.organizer:
        event.delete()
    return redirect('event_list')

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    Registration.objects.get_or_create(event=event, user=request.user)
    return redirect('my_events')

@login_required
def my_events(request):
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'events/my_events.html', {'registrations': registrations})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('event_list')  # Redirect to the event list after signing up
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def event_dashboard(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    registrations = EventRegistration.objects.filter(event=event)
    return render(request, 'events/dashboard.html', {'event': event, 'registrations': registrations})

