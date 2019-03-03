from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import SignUpForm

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			member = authenticate(email=email, password=raw_password)
			login(request, member)
			send_auth_email(email)
			return redirect('/')
	else:
		form = SignUpForm()
	return render(request, 'register.html', {'form': form})

def login_user(request, template_name='registration/login.html', extra_context=None):
	response = auth_views.login(request, template_name)
	if request.POST.has_key('remember_me'):
		request.session.set_expiry(60 * 60 * 24 * 365)

def send_auth_email(user_email):
	email_list = []
	email_list.append(user_email)

	send_mail('Welcome! Autorization Email',
	'Welcome to the Okanagan College Computer Scienence Events and News Page',
	'compscieventsOC@gmail.com',
	email_list,
	fail_silently = False,)