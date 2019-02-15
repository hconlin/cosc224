from django import forms


class NewsForm(forms.Form):
	Name = forms.CharField()
	description = forms.CharField()
	location = forms.CharField()

