from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from members.forms import LoginForm

from . import views

urlpatterns = [
    path('register/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm, redirect_authenticated_user=True), name='login'),
    path('preferences/', views.preference_selection, name='preference_selection'),
    path('<int:pk>/edit/preferences', views.EditPreferences.as_view(), name='edit_preferences'),
    path('<int:user_id>/profile', views.profile, name='member_profile'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('auth/', views.auth_view),

]