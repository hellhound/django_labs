from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^form1/$', 'formapp.views.view1', name='form_view1'),
    url(r'^form2/$', 'formapp.views.view2', name='form_view2'),
    url(r'^view3/$', 'formapp.views.view3', name='view3'),
)
