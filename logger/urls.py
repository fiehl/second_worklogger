from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.logs_list, name='logs_list'),
	url(r'^logs/(?P<pk>\d+)/$',views.logs_detail, name="logs_detail"),
	url(r'^logs/new/$', views.log_new, name='log_new'),
	url(r'^logs/(?P<pk>\d+)/edit/$', views.log_edit,name='log_edit'),
]