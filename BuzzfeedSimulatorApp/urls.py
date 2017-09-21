from django.conf.urls import url
from BuzzfeedSimulatorApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create', views.create, name='create'),
]
