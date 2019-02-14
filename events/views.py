from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from events.forms import EventForm
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
@staff_member_required
def event_form(request):
	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('base')
	else:
		form = EventForm()
	return render(request, 'event.html', {'form': form})