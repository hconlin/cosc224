from django import forms
from news.models import News

class NewsForm(forms.ModelForm):
	title = forms.CharField(label='Title')
	body = forms.CharField(label='Body', widget=forms.Textarea)
	image_link = forms.URLField(label='Image Link')
	
	class Meta:
		model = News
		fields = ['title', 'body', 'image_link']