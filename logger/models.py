# Create your models here.
from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User

class Project(models.Model):
	user = models.ForeignKey('auth.User')
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	

class Logs(models.Model):
	project = models.ForeignKey(Project,on_delete=models.CASCADE)
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	duration = models.FloatField()
	remarks = models.TextField(null=True)
	date = models.DateField(default=date.today)
	total_day = models.FloatField(null=True)

	def __str__(self):
		return "Logs"

	
	def get_total_day(self, request):
		total =[]
		# if self.total_day:
		for dur in Logs.objects.filter(date=date.today(),user=request.user):
			#self.total_day =  total
			#self.save()
			total.append(dur.duration)
		print sum(total)
		self.total_day = sum(total)
		self.save()
	
