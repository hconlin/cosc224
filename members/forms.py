from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label='Email', max_length=200, required=True)
	first_name = forms.CharField(label='First Name', max_length=100, required=True)
	last_name = forms.CharField(label='Last Name', max_length=100, required=True)
	date_of_birth = forms.DateField(label='Date of Birth', widget= forms.SelectDateWidget, required=True)

	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name', 'date_of_birth', 'password1', 'password2')