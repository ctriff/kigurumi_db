from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.studios_list, name='home'),
    url(r'^studios/$', views.studios_list, name="studios_list"),
    url(r'^studios/(?P<pk>\d+)/$', views.get_studio, name="get_studio"),
]
