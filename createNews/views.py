from django.views.generic import TemplateView
from createNews.forms import NewsForm
from django.shortcuts import render


class NewsView(TemplateView):
	template_name = 'createNews/createNews.html'

	def get(self, request):
		form = NewsForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = NewsForm(request.POST)
		text = request.POST['Name']

		args = {'form': form, 'text': text}
		return render(request, self.template_name, args)
