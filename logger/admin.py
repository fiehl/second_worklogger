# Register your models here.
from django.contrib import admin
from .models import Project,Logs

admin.site.register(Project)
admin.site.register(Logs)
