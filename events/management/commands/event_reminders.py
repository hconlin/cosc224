from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from members.models import Member, Preference
from events.models import Event
import datetime
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
DAYS = 2

class Command(BaseCommand):
	help = 'Send Event Reminders'
	def handle(self, *args, **kwargs):
		tomorrows_date =  datetime.date.today() + datetime.timedelta(days=DAYS)
		tomorrows_events = Event.objects.filter(start_date__contains=tomorrows_date)
		for event in tomorrows_events:
			prefered_by_users = Preference.objects.filter(preferences__contains=event.category)
			for user in prefered_by_users:
				obj = Member.objects.get(pk=user.user_id)
				if user.email_activated == 1:
					send_the_mail(obj, event)


def send_the_mail(user, event):
	email_address = user.email
	mail_subject = 'Event Reminder'
	message = render_to_string('email/reminder.html', {
		'user': user,
		'event': event,
	})
	email = EmailMessage(
		mail_subject, message, to=[email_address]
	)
	email.send()