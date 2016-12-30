from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<page_num>[0-9]+)/$', views.index, name='index'),
    url(r'^token/default-labels/(?P<token_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^ambiguous-token/(?P<token_id>[0-9]+)/$', views.ambiguous, name='ambiguous'),
]