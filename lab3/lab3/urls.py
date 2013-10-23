from django.conf.urls import patterns, include, url

from formapp import views

urlpatterns = patterns('',
    url(r'^form1/$', views.View1.as_view(), name='form_view1'),
    url(r'^form2/$', views.View2.as_view(), name='form_view2'),
    url(r'^view3/$', views.View3.as_view(), name='view3'),
)
