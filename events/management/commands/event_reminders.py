from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from members.models import Member, Preference
from events.models import Event
import datetime

class Command(BaseCommand):
	help = 'Send Event Reminders'
	
	def handle(self, *args, **kwargs):

		tomorrows_date =  datetime.date.today() + datetime.timedelta(days=1)
		tomorrows_events = Event.objects.filter(start_date__contains=tomorrows_date)
		print("working")

		for event in tomorrows_events:
			email_list = []
			prefered_by_users = Preference.objects.filter(preferences__contains=event.category)
			for user in prefered_by_users:
				obj = Member.objects.get(pk=user.user_id)
				email_list.append(obj.email)
			send_the_mail(email_list, event)
			print(email_list)



def send_the_mail(email_list, event):
	send_mail('Event Reminder.',
	event.location_details,
	'compscieventsOC@gmail.com',
	email_list,
	fail_silently = False,)