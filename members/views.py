from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from members.models import Preference, Member
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from members.forms import PreferenceForm
from django.utils.decorators import method_decorator
import json
from django.http import HttpResponse

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
			return redirect('/members/preferences/')
	else:
		form = SignUpForm()
	return render(request, 'register.html', {'form': form})

def login_user(request, template_name='registration/login.html', extra_context=None):
	response = auth_views.login(request, template_name)
	if request.POST.has_key('remember_me'):
		request.session.set_expiry(60 * 60 * 24 * 365)

@login_required
def preference_selection(request):
	if Preference.objects.filter(user=request.user).exists():
		return redirect('/members/' + str(request.user.id) + '/edit/preferences')
	else :
		if request.method == 'POST':
			form = PreferenceForm(request.POST)
			if form.is_valid():
				preference = form.save(commit=False)
				preference.user_id = request.user.id
				preference.save()
				messages.add_message(request, messages.INFO, 'Welcome and thanks for joining the Okanagan Collage Computer Science Club', extra_tags='alert-success')
				return redirect('/')
		else:
			form = PreferenceForm()
		return render(request, 'members/preferences.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class EditPreferences(UpdateView):
	model = Preference
	form_class = PreferenceForm
	template_name_suffix = '_edit_form'

	def get_object(self):
		 return Preference.objects.get(user_id=self.request.user.id)

	def get_success_url(self):
		messages.add_message(self.request, messages.INFO, 'Successfully updated your preferences!', extra_tags='alert-success')
		return reverse_lazy('member_profile', kwargs={'user_id': self.request.user.id})

@login_required
def profile(request, user_id):
	member = get_object_or_404(Member, pk=user_id)
	return render(request, 'members/profile.html',{'member': member})

def send_auth_email(user_email):
        email_list = []
        email_list.append(user_email)

        send_mail('Autorization Email',
        'Welcome to the Okanagan College Computer Scienence Events and News Page',
        'compscieventsOC@gmail.com',
        email_list,
        fail_silently = False,)

