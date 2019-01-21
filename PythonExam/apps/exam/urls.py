from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^travels$', views.success),
    url(r'^add$', views.add),
    url(r'^addtrip$', views.addtrip),
    url(r'^view/(?P<id>[0-9]+)$', views.show),
    url(r'^logout$', views.logout),
    url(r'^join/(?P<id>[0-9]+)$', views.join),
    url(r'^cancel/(?P<id>[0-9]+)$', views.cancel),
    url(r'^delete/(?P<id>[0-9]+)$', views.delete),
]