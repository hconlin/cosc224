from django import forms
from events.models import Event

class EventForm(forms.ModelForm):

	EVENT_TYPE = [('Game Competitions', 'Game Competition'),('Software Competitions', 'Software Competition'),
	('Meet and Greets', 'Meet & Greet'),('Seminars', 'Seminar'),
	('Social Networking','Social Networking'), ('Job Fairs', 'Job Fair')]

	title = forms.CharField(label='Title')
	description = forms.CharField(label='Description', widget=forms.Textarea)
	start_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), required=False)
	start_date = forms.DateField(label='Start Date', widget=forms.SelectDateWidget)
	end_date = forms.DateField(label='End Date', widget=forms.SelectDateWidget)
	location = forms.CharField(label='Location Address', required=False)
	location_details = forms.CharField(label='Location Details', widget=forms.Textarea, required=False)
	cost = forms.DecimalField(label='Cost', required=False)
	age_requirement = forms.IntegerField(label='Age Requirement')
	link = forms.URLField(label='Event Link', required=False)
	category = forms.CharField(label='Category', widget=forms.Select(choices=EVENT_TYPE),required=False)
	event_coordinator_name = forms.CharField(label='Contact Name', required=False)
	event_coordinator_email = forms.EmailField(label='Contact Email',required=False)
	image_link = forms.URLField(label='Image Link', required=False)

	class Meta:
		model = Event
		fields = ['title', 'description', 'start_time', 'start_date', 'end_date', 'location', 'location_details',
				  'cost', 'age_requirement', 'link', 'category', 'event_coordinator_name',
				  'event_coordinator_email', 'image_link']

	def clean(self):
		cleaned_data = super().clean()
		start_date = cleaned_data.get("start_date")
		end_date = cleaned_data.get("end_date")
		if end_date < start_date:
			msg = u"End date should be later than start date."
			self._errors["end_date"] = self.error_class([msg])




