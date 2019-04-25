from django import forms
from events.models import Event

class EventForm(forms.ModelForm):

	EVENT_TYPE = [('Game Competitions', 'Game Competition'),('Software Competitions', 'Software Competition'),
	('Meet and Greets', 'Meet & Greet'),('Seminars', 'Seminar'),
	('Social Networking','Social Networking'), ('Job Fairs', 'Job Fair')]

	HOURS = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')]

	MINUTES = [('00', '00'), ('15', '15'), ('30', '30'), ('45', '45')]

	MERIDIEMS = [('AM', 'AM'), ('PM', 'PM')]

	AGE_REQS = [('None', 'None'), ('Must be older than', 'Must be older than'), ('Must be younger than', 'Must be younger than')]

	title = forms.CharField(label='Title')
	description = forms.CharField(label='Description', widget=forms.Textarea)
	hour = forms.CharField(label='Hour', widget=forms.Select(choices=HOURS, attrs={'class': 'time-input'}))
	minute = forms.CharField(label='Minute', widget=forms.Select(choices=MINUTES, attrs={'class': 'time-input'}))
	meridiem = forms.CharField(label='Meridiem', widget=forms.Select(choices=MERIDIEMS, attrs={'class': 'time-input'}))
	start_date = forms.DateField(label='Start Date', widget=forms.SelectDateWidget)
	end_date = forms.DateField(label='End Date', widget=forms.SelectDateWidget)
	location = forms.CharField(label='Location Address', required=False)
	location_details = forms.CharField(label='Location Details', widget=forms.Textarea, required=False)
	cost = forms.DecimalField(label='Cost', required=False)
	age_requirement = forms.CharField(label='Age Requirement', widget=forms.Select(choices=AGE_REQS, attrs={'class': 'age-requirement'}))
	age = forms.CharField(widget=forms.HiddenInput(), label='', required=False)
	link = forms.URLField(label='Event Link', required=False)
	category = forms.CharField(label='Category', widget=forms.Select(choices=EVENT_TYPE),required=False)
	event_coordinator_name = forms.CharField(label='Contact Name', required=False)
	event_coordinator_email = forms.EmailField(label='Contact Email',required=False)
	image_link = forms.URLField(label='Image Link', required=False)

	class Meta:
		model = Event
		fields = ['title', 'description', 'hour', 'minute', 'meridiem', 'start_date', 'end_date', 'location', 'location_details',
				  'cost', 'age_requirement', 'age','link', 'category', 'event_coordinator_name',
				  'event_coordinator_email', 'image_link']

	def clean(self):
		cleaned_data = super().clean()
		start_date = cleaned_data.get("start_date")
		end_date = cleaned_data.get("end_date")
		if end_date < start_date:
			msg = u"End date should be later than start date."
			self._errors["end_date"] = self.error_class([msg])




