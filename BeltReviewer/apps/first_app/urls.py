from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^$', views.index),
		url(r'^create$', views.create),
		url(r'^home$', views.home),
		url(r'^read$', views.read),
		url(r'^displayAdd', views.displayAddReview),
		url(r'^logoff$', views.logoff),
		url(r'^processBnR$', views.processBnR),
		url(r'^bookInfo/(?P<id>\d+)$', views.bookInfo),
		url(r'^processR/(?P<id>\d+)$', views.processR),
		url(r'^userInfo/(?P<id>\d+)$', views.userInfo)


]