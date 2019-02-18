from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.event_form, name='create'),
    path('<int:event_id>', views.show, name='show'),
    path('<int:pk>/edit', views.EditEvent.as_view(), name='edit')
]