from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
	email = forms.EmailField(max_length=200, required=True)
	first_name = forms.CharField(max_length=100, required=True)
	last_name = forms.CharField(max_length=100, required=True)
	date_of_birth = forms.DateField()

	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name', 'date_of_birth', 'password1', 'password2')