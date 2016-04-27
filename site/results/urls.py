from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^(?P<runner_id>[0-9]+)/$', views.detail, name='detail'),
        url(r'^(?P<runner_id>[0-9]+)/results/$', views.results, name='results'),
        url(r'^races/$', views.races, name='races'),
        url(r'^race/(?P<race_id>[0-9]+)/$', views.race, name='race'),
        url(r'^(?P<runner_id>[0-9]+)/addresult/$', views.addresult, name='addresult'),
]
