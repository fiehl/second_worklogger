from django import forms
from .models import Logs

class LogsForm(forms.ModelForm):
	class Meta:
		model = Logs
		fields = ('duration', 'project','remarks')