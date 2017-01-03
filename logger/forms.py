from django import forms
from .models import Project,Logs
from django.contrib.auth.forms import UserCreationForm

class LogsForm(forms.ModelForm):
	class Meta:
		model = Logs
		fields = ('duration', 'project','remarks','date')

class SignUpForm(UserCreationForm):
	email = forms.EmailField(
		required=True, widget=forms.TextInput(attrs={'class':'form-control'})
	)
	username = forms.CharField(
		widget=forms.TextInput(attrs={'class':'form-control'})
	)
	password1=forms.CharField(
		widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
	)
	password2=forms.CharField(
		widget=forms.TextInput(attrs={'class':'form-control','type':'password'})
	)
