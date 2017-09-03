from django.conf.urls import url

from gornany import views

urlpatterns = [
    # ex: /gornany/
    url(r'^$', views.index, name='index'),
]