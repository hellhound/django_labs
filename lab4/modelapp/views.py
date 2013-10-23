# -*- coding:utf-8 -*-
from django.views.generic.edit import CreateView, \
    UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy

from modelapp.models import A


class CreateAView(CreateView):
    model = A
    success_url = reverse_lazy('list_a')


class EditAView(UpdateView):
    model = A
    success_url = reverse_lazy('list_a')


class ListAView(ListView):
    model = A


class DeleteAView(DeleteView):
    model = A
    success_url = reverse_lazy('list_a')
