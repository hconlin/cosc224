from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from events.forms import EventForm
from django.contrib.admin.views.decorators import staff_member_required
from events.models import Event

# Create your views here.
@staff_member_required
def event_form(request):
	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			event = form.save(commit=False)
			event.user_id = request.user
			event.save()
			return HttpResponseRedirect('/events/' + str(event.id))
	else:
		form = EventForm()
	return render(request, 'event.html', {'form': form})

def show(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	return render(request, 'show.html',{'event': event})
