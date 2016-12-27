from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.logs_list, name='logs_list'),
	url(r'^logs/(?P<pk>\d+)/$',views.logs_detail, name="logs_detail"),
]