from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.event_form, name='event'),
]