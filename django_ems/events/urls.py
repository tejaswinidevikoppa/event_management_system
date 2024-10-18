from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('create/', views.event_create, name='event_create'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/register/', views.register_for_event, name='register_for_event'),
    path('my-events/', views.my_events, name='my_events'),
    path('signup/', views.signup, name='signup'),
]
    
