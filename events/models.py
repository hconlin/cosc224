from django.db import models
from members.models import Member

class Event(models.Model):
	user_id = models.IntegerField()
	title = models.CharField(max_length=200)
	description = models.TextField(max_length = 2000)
	start_time = models.TimeField()
	start_date = models.DateField()
	end_date = models.DateField()
	location = models.CharField(max_length=200)
	location_details = models.TextField(max_length=2000)
	cost = models.DecimalField(max_digits=8, decimal_places=2, null=True)
	age_requirement = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	category = models.CharField(max_length=200)
	event_coordinator_name = models.CharField(max_length=200)
	event_coordinator_email = models.EmailField()
	image_link = models.CharField(max_length=200)
	REQUIRED_FIELDS = ['title', 'start_date', 'end_date', 'age_requirement', 'category']

class HomePageEvent(models.Model):
	user_id = models.IntegerField()
	title = models.CharField(max_length=200)
	description = models.TextField(max_length = 2000)
	start_time = models.TimeField()
	start_date = models.DateField()
	end_date = models.DateField()
	location = models.CharField(max_length=200)
	location_details = models.TextField(max_length=2000)
	cost = models.DecimalField(max_digits=8, decimal_places=2,null=True)
	age_requirement = models.IntegerField()
	link = models.CharField(max_length=200)
	category = models.CharField(max_length=200)
	event_coordinator_name = models.CharField(max_length=200)
	event_coordinator_email = models.EmailField()
	image_link = models.CharField(max_length=200)
	active = models.BooleanField(default=False)
	REQUIRED_FIELDS = ['title', 'start_date', 'end_date', 'age_requirement', 'category']

	def update(self, newEvent):
			self.user_id = newEvent.user_id
			self.title = newEvent.title
			self.description = newEvent.description
			self.start_time = newEvent.start_time
			self.start_date = newEvent.start_date
			self.end_date = newEvent.end_date
			self.location = newEvent.location
			self.location_details = newEvent.location_details
			self.cost = newEvent.cost
			self.age_requirement = newEvent.age_requirement
			self.link = newEvent.link
			self.category = newEvent.category
			self.event_coordinator_name = newEvent.event_coordinator_name
			self.event_coordinator_email = newEvent.event_coordinator_email
			self.image_link = newEvent.image_link
			self.active = True
			self.save()

