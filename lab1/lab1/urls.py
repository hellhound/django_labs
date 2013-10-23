from django.conf.urls import patterns, include, url

from app1.views import view

urlpatterns = patterns('',
    (r'^view1/$', 'app1.views.view'),
    (r'^view2/$', view),
)
