from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from members.models import Member
from events.models import Event

class Command(BaseCommand):
	help = 'Send Event Reminders'
	
	def handle(self, *args, **kwargs):
		







def send_the_mail(email_list, event_details):
	send_mail('Event Reminder.',
	event_details,
	'compscieventsOC@gmail.com',
	MUST BE LIST,
	fail_silently = False,)