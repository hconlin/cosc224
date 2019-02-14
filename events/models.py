from django.db import models
from members.models import Member

# Create your models here.
class Event(models.Model):
	user_id = models.ForeignKey(Member, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	start_time = models.TimeField()
	start_date = models.DateField()
	end_date = models.DateField()
	location = models.CharField(max_length=200)
	location_details = models.TextField(max_length=2000)
	cost = models.DecimalField(max_digits=8, decimal_places=2)
	age_requirement = models.IntegerField()
	link = models.CharField(max_length=200)
	category = models.CharField(max_length=200)
	event_coordinator_name = models.CharField(max_length=200)
	event_coordinator_email = models.EmailField()
	image_link = models.CharField(max_length=200)
