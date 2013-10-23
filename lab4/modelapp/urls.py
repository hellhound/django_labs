# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url

from modelapp import views

urlpatterns = patterns('',
    url(r'^a/new/$', views.CreateAView.as_view(),
        name='new_a'),
    url(r'^a/edit/(?P<pk>\d+)/$', views.EditAView.as_view(),
        name='edit_a'),
    url(r'^a/$', views.ListAView.as_view(),
        name='list_a'),
    url(r'^a/delete/(?P<pk>\d+)/$',
        views.DeleteAView.as_view(),
        name='delete_a'),
)
