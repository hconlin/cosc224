from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm, ProfileForm, EditPasswordForm
from django.contrib.auth.decorators import login_required
from members.models import Preference, Member
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from members.forms import PreferenceForm
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.contrib import auth
from django.db import connection
from threading import Thread
import string
import random
from django.contrib.auth.hashers import make_password
import json

N = 32


def start_new_thread(function):
	def decorator(*args, **kwargs):
		t = Thread(target=function, args=args, kwargs=kwargs)
		t.daemon = True
		t.start()

	return decorator


def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user_salt = gimme_salt()
			user.user_salt = user_salt
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			salted_pass = raw_password + user_salt
			user.password = make_password(salted_pass)
			user.save()
			member = authenticate(email=email, password=salted_pass)
			login(request, member)
			current_site = get_current_site(request)
			current_site = current_site.domain
			send_verification_email(member.id, current_site)

			return redirect('/preferences/')
	else:
		form = SignUpForm()
	return render(request, 'register.html', {'form': form})


@start_new_thread
def send_verification_email(user_id, current_site_domain):
	user = Member.objects.get(pk=user_id)
	email_address = user.email
	mail_subject = 'Activate your account.'
	message = render_to_string('email/acc_active_email.html', {
		'user': user,
		'domain': current_site_domain,
		'uid': urlsafe_base64_encode(force_bytes(user_id)).decode(),
		'token': account_activation_token.make_token(user),
	})
	email = EmailMessage(
		mail_subject, message, to=[email_address]
	)
	email.send()
	connection.close()


@login_required
def preference_selection(request):
	if Preference.objects.filter(user=request.user).exists():
		return redirect('/edit/preferences')
	else:
		if request.method == 'POST':
			form = PreferenceForm(request.POST)
			if form.is_valid():
				preference = form.save(commit=False)
				preference.user_id = request.user.id
				preference.save()
				messages.add_message(request, messages.INFO,
									 'Welcome and thanks for joining the Okanagan Collage Computer Science Club',
									 extra_tags='alert-success')
				return redirect('/')
		else:
			form = PreferenceForm()
		return render(request, 'members/preferences.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class EditProfile(UpdateView):
	model = Member
	form_class = ProfileForm
	template_name_suffix = '_edit_form'

	def get_object(self):
		return Member.objects.get(id=self.request.user.id)

	def get_success_url(self):
		messages.add_message(self.request, messages.INFO, 'Successfully updated your info!', extra_tags='alert-success')
		return reverse_lazy('member_profile')


@method_decorator(login_required, name='dispatch')
class EditPreferences(UpdateView):
	model = Preference
	form_class = PreferenceForm
	template_name_suffix = '_edit_form'

	def get_object(self):
		return Preference.objects.get(user_id=self.request.user.id)

	def get_success_url(self):
		messages.add_message(self.request, messages.INFO, 'Successfully updated your preferences!',
							 extra_tags='alert-success')
		return reverse_lazy('member_profile')


@login_required
def profile(request):
	member = get_object_or_404(Member, pk=request.user.id)
	return render(request, 'members/profile.html', {'member': member})


def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = Member.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.email_activated = True
		user.save()
		login(request, user)
		return render(request, 'email/confirmation.html', {'answer': 'Your Registration is Complete! Thanks.'})
	else:
		return render(request, 'email/confirmation.html', {'answer': 'Invalid link, please resend email INSERT BUTTON'})


def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = Member.objects.filter(email=username)
	if Member.objects.filter(email=username).exists():
		print(user[0].user_salt)
		salt = user[0].user_salt
		password = password + salt
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				auth.login(request, user)
				return redirect('/')
		#email password are incorrect
		else:
			messages.add_message(request, messages.INFO, 'Invalid email and password.', extra_tags='alert-danger')
			return redirect('/login')
	#email does not exists
	else:
		messages.add_message(request, messages.INFO, 'Invalid email and password.', extra_tags='alert-danger')
		return redirect('/login')

def gimme_salt():
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))


#needs to be fixed
def change_password(request):
    if request.method == 'POST':
        form = EditPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.add_message(request, messages.INFO, 'Success.', extra_tags='alert-success')
            return redirect('member_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = EditPasswordForm(request.user)
    return render(request, 'members/change_password.html', {
        'form': form
    })
