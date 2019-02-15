from django.conf.urls import url
from createEvent.views import EventView

urlpatterns = [
   url(r'^$', EventView.as_view(), name = 'createEvent'),

]
