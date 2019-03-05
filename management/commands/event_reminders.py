from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from members.models import Member, Preference
from events.models import Event

class Command(BaseCommand):
	help = 'Send Event Reminders'
	
	def handle(self, *args, **kwargs):
		all_users = Member.objects.all()
		#get all events that happen tomorrow
		#get all users who are interested in event
		#build message about event and build list of members 
		tomorrows_date =  datetime.date.today() + datetime.timedelta(days=1)
		tomorrows_events = Events.objects.filter(start_date__contains=tomorrows_date)

		#for event_tomorrow in tomorrows_events:








def send_the_mail(email_list, event_details):
	send_mail('Event Reminder.',
	event_details,
	'compscieventsOC@gmail.com',
	MUST BE LIST,
	fail_silently = False,)