
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
			hour = form['hour'].value()
			minute = form['minute'].value()
			meridiem = form['meridiem'].value()
			if meridiem == 'PM' and not int('0' + hour) == 12:
				hour = int('0' + hour) + 12
				hour = str(hour)
			elif meridiem == 'AM' and int('0' + hour) == 12:
				hour = int('0' + hour) - 12
				hour = str(hour)
			age_requirement = form['age_requirement'].value()
			age = form['age'].value()
			if age_requirement == 'Must be older than' or age_requirement == 'Must be younger than':
				age_requirement = str(age_requirement + " " + str(age) + " year(s) old")
			else:
				age_requirement = str(age_requirement)
			event = form.save(commit=False)
			start_time = str(hour + ':' + minute + " " + meridiem)
			event.start_time = start_time
			event.age_requirement = age_requirement
			event.user_id = request.user.pk
			event.save()
			messages.add_message(request, messages.INFO, 'Event successfully created!', extra_tags='alert-success')
			return HttpResponseRedirect('/events/' + str(event.id))
	else:
		form = EventForm()
	return render(request, 'events/event.html', {'form': form})

def event_edit(request, pk):
	homepage = HomePageEvent.objects.first()

	instance = Event.objects.get(pk=pk)
	form = EventForm(request.POST or None, instance=instance)
	if form.is_valid():
		hour = form['hour'].value()
		minute = form['minute'].value()
		meridiem = form['meridiem'].value()
		if meridiem == 'PM' and not int('0' + hour) == 12:
			hour = int('0' + hour) + 12
			hour = str(hour)
		elif meridiem == 'AM' and int('0' + hour) == 12:
			hour = int('0' + hour) - 12
			hour = str(hour)
		age_requirement = form['age_requirement'].value()
		age = form['age'].value()
		if age_requirement == 'Must be older than' or age_requirement == 'Must be younger than':
			age_requirement = str(age_requirement + " " + str(age) + " year(s) old")
		else:
			age_requirement = str(age_requirement)
		event = form.save(commit=False)
		start_time = str(hour + ':' + minute + " " + meridiem)
		event.start_time = start_time
		event.age_requirement = age_requirement
		event.user_id = request.user.pk
		event.save()
		
		if instance.pk == homepage.event_id:
			homepage.update(instance)


		messages.add_message(request, messages.INFO, 'Successfully saved changes!', extra_tags='alert-success')
		return HttpResponseRedirect('/events/' + str(event.id))
	return render(request, 'events/event_edit_form.html', {'event': instance, 'form': form})

def show(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	return render(request, 'events/show.html',{'event': event})

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
		eventselected = request.POST.get('settings')

		if eventselected == 'upcoming' and eventPicked:
			eventPicked.active = False
			eventPicked.save()
		elif eventselected == 'set':
			
			chosenEvent = request.POST.get('eventselect')
			
			if eventPicked:	
				eventPicked.update(upcoming.get(pk=chosenEvent))
			
		messages.add_message(request, messages.INFO, 'Home Page Updated!', extra_tags='alert-success')


	return render(request, 'adminpanel.html', context)
