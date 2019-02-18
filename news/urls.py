from django.urls import path
from . import views

urlpatterns = [
    path('news/create/', views.news_form, name='create'),
    path('<int:news_id>', views.show, name='show'),
    path('<int:pk>/edit', views.EditNews.as_view(), name='edit'),
]