from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.event_form, name='create_event'),
    path('<int:event_id>', views.show, name='show_event'),
    path('<int:pk>/edit', views.EditEvent.as_view(), name='edit_event'),
    path('<int:event_id>/delete', views.deleteEvent, name='delete_event'),
    path('', views.events, name='events'),
]