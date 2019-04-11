
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from events.forms import EventForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from events.models import *
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
@staff_member_required
def event_form(request):
	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			event = form.save(commit=False)
			event.user_id = request.user.pk
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
	now = timezone.now()
	setEvent = HomePageEvent.objects.first()
	upcomingEvent = Event.objects.filter(start_date__gte=now).order_by('start_date').first()
	


	#If event is set
	if setEvent and setEvent.active == True:
			context = {
				'events': setEvent,
			}
	#Else display most recent	
	elif upcomingEvent:
			context = {
				'events': upcomingEvent,
			}
	#Empty Database
	else:
		context ={

		}

	return render(request, 'events/home.html', context)


def events(request):
	#currently iterates through all events. 
	context = {
		'events': Event.objects.all().order_by('-start_date')
	}
	return render(request, 'events/events.html', context)

@login_required(login_url='/login')
def settings(request):
	now = timezone.now()
	upcoming = Event.objects.filter(start_date__gte=now).order_by('-start_date')
	eventPicked = HomePageEvent.objects.first()

	context = {
		'upcomingEvents': upcoming,
		'setEvent': eventPicked
	}
	

	if request.method == 'POST':
		selected = request.POST.get('settings')

		if selected == 'upcoming' and eventPicked:
			eventPicked.active = False
			eventPicked.save()
		elif selected == 'set':
			
			chosenEvent = request.POST.get('eventselect')
			
			if eventPicked:	
				eventPicked.update(upcoming.get(pk=chosenEvent))
			
		messages.add_message(request, messages.INFO, 'Home Page Updated!', extra_tags='alert-success')


	return render(request, 'events/set_home_event.html', context)
