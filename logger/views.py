from django.shortcuts import render
from .models import Project,Logs 
from django.utils import timezone

# Create your views here.
def logs_list(request):
	logs = Logs.objects.filter(date__gte=timezone.now()).order_by('-date')
	return render(request,'logs/logs_list.html',{'logs':logs})