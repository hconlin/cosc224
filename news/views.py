from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from news.forms import NewsForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from datetime import datetime
from news.models import News
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages

@staff_member_required
def news_form(request):
	if request.method == 'POST':
		form = NewsForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			news = form.save(commit=False)
			news.author_id = request.user
			news.date = datetime.now()
			news.save()
			messages.add_message(request, messages.INFO, 'News successfully created!', extra_tags='alert-success')
			return HttpResponseRedirect('/news/' + str(news.id))
	else:
		form = NewsForm()
	return render(request, 'news/news.html', {'form': form})

def show(request, news_id):
	news = get_object_or_404(News, pk=news_id)
	return render(request, 'news/show.html', {'news': news})

@method_decorator(staff_member_required, name='dispatch')
class EditNews(UpdateView):
    model = News
    form_class = NewsForm
    template_name_suffix = '_edit_form'

    def get_success_url(self):
    	messages.add_message(self.request, messages.INFO, 'News successfully updated!', extra_tags='alert-success')
    	return reverse_lazy('show_news', kwargs={'news_id': self.object.pk})

@staff_member_required
def deleteNews(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    news.delete()
    messages.add_message(request, messages.INFO, 'News successfully deleted!', extra_tags='alert-success')
    return HttpResponseRedirect('/')

def news(request):
	#currently iterates through all events. 
	context = {
		'news': News.objects.all()
	}
	return render(request, 'news/newz.html', context)
