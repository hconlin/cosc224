from django.urls import path
from django.contrib.auth import views as auth_views
from members.forms import LoginForm

from . import views

urlpatterns = [
    path('register/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm, redirect_authenticated_user=True), name='login'),
]