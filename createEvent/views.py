from django.views.generic import TemplateView
from createEvent.forms import EventForm
from django.shortcuts import render


class EventView(TemplateView):
	template_name = 'createEvent/createEvent.html'

	def get(self, request):
		form = EventForm()
		return render(request, self.template_name, {'form': form})
	
	def post(self, request):
		form = EventForm(request.POST)
		text = request.POST['Name']

		args = {'form': form, 'text': text}
		return render(request, self.template_name, args)
