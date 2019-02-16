from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from news.forms import NewsForm
from django.contrib.admin.views.decorators import staff_member_required
from datetime import datetime
from news.models import News

# Create your views here.
@staff_member_required
def news_form(request):
	if request.method == 'POST':
		form = NewsForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			news = form.save(commit = False)
			news.author_id = request.user
			news.date = datetime.now()
			news.save()
			return HttpResponseRedirect('/news/' + str(news.id))
	else:
		form = NewsForm()
	return render(request, 'news.html', {'form': form})

def show(request, news_id):
	news = get_object_or_404(News, pk=news_id)
	return render(request, 'show.html', {'news': news})
