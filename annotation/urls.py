from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<page_num>[0-9]+)/$', views.index, name='index'),
    url(r'^token/default-labels/(?P<token_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^token/do-label/(?P<token_id>[0-9]+)/$', views.default_annotation, name='do-label'),
    url(r'^ambiguous/$', views.ambiguous, name='ambiguous'),
    url(r'^ambiguous-detail/(?P<token_id>[0-9]+)/$', views.ambiguous_detail, name='ambiguous-detail'),
    url(r'^occurrence/(?P<occur_id>[0-9]+)/$', views.occurrence,
        name='occurrence'),
]
