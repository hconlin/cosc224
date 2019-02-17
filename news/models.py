from django.db import models
from members.models import Member

class News(models.Model):
	author_id = models.ForeignKey(Member, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	date = models.DateField()
	body = models.TextField(max_length=2000)
	image_link = models.CharField(max_length=200)

	def __str__(self):
		return self.title
