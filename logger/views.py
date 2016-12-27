from django.shortcuts import render, redirect
from .models import Project,Logs 
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import LogsForm
# Create your views here.
def logs_list(request):
	logs = Logs.objects.filter(date__gte=timezone.now()).order_by('-date')
	return render(request,'logs/logs_list.html',{'logs':logs})

def logs_detail(request,pk):
	log = get_object_or_404(Logs, pk=pk)
	print log
	return render(request, 'logs/log_detail.html', {'log':log})

def log_new(request):
	if request.method == "POST":
		form= LogsForm(request.POST)
		if form.is_valid():
			log = form.save(commit=False)
			log.user = request.user
			log.date = timezone.now()
			log.save()
			return redirect('logs_list')
	else:
		form = LogsForm()
	return render(request, 'logs/log_edit.html', {'form':form})

def log_edit(request, pk):

	log = get_object_or_404(Logs, pk=pk)
	if request.method =="POST":
		form = LogsForm(request.POST, instance=log)
		if form.is_valid():
			log = form.save(commit=False)
			log.user = request.user
			log.date = timezone.now()
			log.save()
			return redirect('logs_list')
	else:
		form = LogsForm(instance=log)
	return render(request, 'logs/log_edit.html', {'form':form})