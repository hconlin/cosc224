from django.conf.urls import url
from createNews.views import NewsView

urlpatterns = [
   url(r'^$', NewsView.as_view() , name = 'createNews')
]
