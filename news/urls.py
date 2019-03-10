from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.news_form, name='create_news'),
    path('<int:news_id>', views.show, name='show_news'),
    path('<int:pk>/edit', views.EditNews.as_view(), name='edit_news'),
    path('<int:news_id>/delete', views.deleteNews, name='delete_news'),
    path('', views.news, name='news')
]
