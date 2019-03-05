from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from members.models import Preference, Member

User = get_user_model()

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label='Email', max_length=200, required=True,
							 widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Email'}))
	first_name = forms.CharField(label='First Name', max_length=100, required=True,
								 widget=forms.TextInput(attrs={'autofocus':'autofocus','class': 'form-input half', 'placeholder': 'First name'}))
	last_name = forms.CharField(label='Last Name', max_length=100, required=True,
								widget=forms.TextInput(attrs={'class': 'form-input half', 'placeholder': 'Last name'}))
	date_of_birth = forms.DateField(label='Date of Birth', widget=forms.SelectDateWidget(attrs={'class': 'date-input'}), required=True)
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Confirm Password'}))

	class Meta:
		model = User
		fields = ('first_name', 'last_name','email', 'password1', 'password2', 'date_of_birth')

class LoginForm(AuthenticationForm):
	username = forms.EmailField(widget=forms.TextInput(attrs={'autofocus':'autofocus','class': 'form-input', 'placeholder': 'Email'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'}))


class PreferenceForm(forms.ModelForm):
	PREFERENCES = (('game competitions', 'Game Competitions'),('software competitions', 'Software Competitions'),('meet and greets', 'Meet & Greets'),('seminars', 'Seminars'),
					('social networking','Social Networking'), ('job fairs', 'Job Fairs'))
	preferences = forms.MultipleChoiceField(choices=PREFERENCES, widget=forms.CheckboxSelectMultiple(attrs={'class':'checkmark'}))

	class Meta:
		model = Preference
		fields = ('preferences',)

