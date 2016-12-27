from django.shortcuts import render
from .models import Project,Logs 
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
# Create your views here.
def logs_list(request):
	logs = Logs.objects.filter(date__gte=timezone.now()).order_by('-date')
	return render(request,'logs/logs_list.html',{'logs':logs})

def logs_detail(request,pk):
	log = get_object_or_404(Logs, pk=pk)
	print log
	return render(request, 'logs/log_detail.html', {'log':log})