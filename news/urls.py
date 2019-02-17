from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.news_form, name='create'),
    path('<int:news_id>', views.show, name='show')
]