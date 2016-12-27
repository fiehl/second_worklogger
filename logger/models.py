# Create your models here.
from django.db import models
from django.utils import timezone

class Project(models.Model):
	user = models.ForeignKey('auth.User')
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Logs(models.Model):
	project = models.ForeignKey(Project,on_delete=models.CASCADE)
	duration = models.FloatField()
	remarks = models.TextField(null=True)
	total_day = models.IntegerField()
	date = models.DateField(default=timezone.now)

	def __str__(self):
		return self.date		