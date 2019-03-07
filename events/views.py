from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from events.forms import EventForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from events.models import Event
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages

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
			messages.add_message(request, messages.INFO, 'Event successfully created!', extra_tags='alert-success')
			return HttpResponseRedirect('/events/' + str(event.id))
	else:
		form = EventForm()
	return render(request, 'events/event.html', {'form': form})

def show(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	return render(request, 'events/show.html',{'event': event})

@method_decorator(staff_member_required, name='dispatch')
class EditEvent(UpdateView):
	model = Event
	form_class = EventForm
	template_name_suffix = '_edit_form'

	def get_success_url(self):
		messages.add_message(self.request, messages.INFO, 'Event successfully updated!', extra_tags='alert-success')
		return reverse_lazy('show_event', kwargs={'event_id': self.object.pk})

@staff_member_required
def deleteEvent(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.add_message(request, messages.INFO, 'Event successfully deleted!', extra_tags='alert-success')
    return HttpResponseRedirect('/')

def home(request):
	#currently iterates through all events. 
	context = {
		'events': Event.objects.all()[:1]
	}
	return render(request, 'events/home.html', context)


def events(request):
	#currently iterates through all events. 
	context = {
		'events': Event.objects.all()
	}
	return render(request, 'events/events.html', context)
