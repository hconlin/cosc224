from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from members.models import Member

class Command(BaseCommand):
	help = 'Send Auth Email'
	
	def handle(self, *args, **kwargs):
		all_users = Member.object.all()

		for user in all_users:
			
			send_mail('Hello From Andrews Test',
			'This is a test',
			'compscieventsOC@gmail.com',
			all_emails,
			fail_silently = False,)





