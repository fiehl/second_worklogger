from django.shortcuts import render, redirect
from .models import Project,Logs
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import LogsForm,SignUpForm
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def logs_list(request):
	total = 0
	total_week =0
	total_month =0
	logs = Logs.objects.filter(date=timezone.now(),user=request.user).order_by('-date') 
	
	
	if request.method == "POST":
		form= LogsForm(request.POST)
		if form.is_valid():
			log = form.save(commit=False)
			log.user = request.user
			#log.date = timezone.now()
			
			log.save()
			log.get_total_day(request)
			log.get_total_week(request)
			log.get_total_month(request)
			return redirect('logs_list')
	else:
		form = LogsForm()
	for log in logs:
		log.get_total_day(request)
		log.get_total_week(request)
		log.get_total_month(request)
		total = log.total_day
		total_week = log.total_week
		total_month = log.total_month
	return render(request,'logs/logs_list.html',{'logs':logs,'total':total,'form':form,'total_week':total_week,'total_month':total_month})

def logs_delete(request,pk):
	logs= Logs()
	log = get_object_or_404(Logs, pk=pk)
	if request.method == "POST":

		log.delete()

		return redirect('logs_list')
	return render(request, 'logs/log_detail.html', {'log':log})

def go_to(request,date):
	logs = Logs.objects.filter(date=timezone.now()).order_by('-date')
 	return render(request,'logs/logs_list.html',{'logs':logs}) 
# def log_new(request):
	
# 	if request.method == "POST":
# 		form= LogsForm(request.POST)
# 		if form.is_valid():
# 			log = form.save(commit=False)
# 			log.user = request.user
# 			log.date = timezone.now()
			
# 			log.save()
# 			log.get_total_day()
			
# 			return redirect('logs_list')
# 	else:
# 		form = LogsForm()
# 	return render(request, 'logs/log_edit.html', {'form':form})
@login_required
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
	return render(request, 'logs/logs_list.html', {'form':form})

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign_up.html'

    def form_valid(self,form):
        form.save()
        return super(SignUpView, self).form_valid(form)