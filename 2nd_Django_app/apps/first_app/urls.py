from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^display$', views.index),
url(r'^new-display$', views.new),
url(r'^create$', views.create),
url(r'^(?P<num>[0-9]+)$', views.showNum),
url(r'^edit/(?P<num>[0-9]+)$', views.editNum),
url(r'^delete/(?P<num>[0-9]+)$', views.deleteNum)
]