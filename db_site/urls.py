from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.studios_list, name='home'),
    url(r'^studios/$', views.studios_list, name="studios_list"),
]
