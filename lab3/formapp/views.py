# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic.base import View, TemplateView
from django.views.generic.edit import FormView

from formapp.forms import Form


class View1(FormView):
    template_name = 'formapp/form.html'
    form_class = Form

    def form_valid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form))


class View2(FormView):
    form_class = Form
    template_name = 'formapp/form.html'

    def get_success_url(self):
        return reverse('view3')


class View3(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(u'Felicitaciones, funcionó!')
