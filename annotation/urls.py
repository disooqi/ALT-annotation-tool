from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<page_num>[0-9]+)/$', views.index, name='index'),
]