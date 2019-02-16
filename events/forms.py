from django import forms
from events.models import Event

class EventForm(forms.ModelForm):
	title = forms.CharField(label='Title')
	start_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), required=False)
	start_date = forms.DateField(label='Start Date', widget=forms.SelectDateWidget)
	end_date = forms.DateField(label='End Date', widget=forms.SelectDateWidget)
	location = forms.CharField(label='Location Address')
	location_details = forms.CharField(label='Location Details', widget=forms.Textarea)
	cost = forms.DecimalField(label='Cost')
	age_requirement = forms.IntegerField(label='Age Requirement')
	link = forms.URLField(label='Event Link')
	category = forms.CharField(label='Category')
	event_coordinator_name = forms.CharField(label='Contact Name')
	event_coordinator_email = forms.EmailField(label='Contact Email')
	image_link = forms.URLField(label='Image Link')

	class Meta:
		model = Event
		fields = ('title', 'start_time', 'start_date', 'end_date', 'location', 'location_details',
				  'cost', 'age_requirement', 'link', 'category', 'event_coordinator_name',
				  'event_coordinator_email', 'image_link')
