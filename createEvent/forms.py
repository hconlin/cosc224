from django import forms


class EventForm(forms.Form):
	Name = forms.CharField()
	time = forms.DateField()
	description = forms.CharField()
	location = forms.CharField()

