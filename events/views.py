from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from events.forms import EventForm
from django.contrib.admin.views.decorators import staff_member_required
from events.models import Event
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

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
	return render(request, 'events/event.html', {'form': form})

def show(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	return render(request, 'events/show.html',{'event': event})

@staff_member_required
class EditEvent(UpdateView):
	model = Event
	form_class = EventForm
	template_name_suffix = '_edit_form'

	def get_success_url(self):
		return reverse_lazy('show', kwargs={'event_id': self.object.pk})