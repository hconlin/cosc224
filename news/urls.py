from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.news_form, name='news'),
    path('<int:news_id>', views.show, name='show')
]