# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect

from formapp.forms import Form


def view1(request):
    if request.method.lower() == 'get':
        return render(request, 'formapp/form.html',
            dict(form=Form()))
    return render(request, 'formapp/form.html',
        dict(form=Form(data=request.POST)))


def view2(request):
    data = None
    if request.method.lower() == 'post':
        data = request.POST
        form = Form(data=data)
        if form.is_valid():
            return redirect('view3')
    return render(request, 'formapp/form.html',
        dict(form=Form(data=data)))


def view3(request):
    return HttpResponse(u'Felicitaciones, funcionó!')
