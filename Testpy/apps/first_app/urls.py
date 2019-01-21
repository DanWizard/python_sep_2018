from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^$', views.index),
		url(r'^create$', views.create),
		url(r'^home$', views.home),
		url(r'^read$', views.read),
		url(r'^logoff$', views.logoff),
		url(r'^addJob$', views.addJob),
		url(r'^processAdd$', views.processAdd),
		url(r'^view/(?P<id>\d+)$', views.displayView),
		url(r'^edit/(?P<id>\d+)$', views.displayEdit),
		url(r'^remove/(?P<id>\d+)$', views.delete),
		url(r'^processEdit/(?P<id>\d+)$', views.processEdit),
		url(r'^errors$', views.displayEditwErrors)

]