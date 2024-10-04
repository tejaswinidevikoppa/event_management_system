# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Registration
from .forms import EventForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.isValid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_create.html', {'form': form})

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
