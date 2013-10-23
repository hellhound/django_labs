# -*- coding:utf-8 -*-
from django.http import HttpResponse

def view(request):
    if request.method.lower() == 'get':
        return HttpResponse(u'Hola mundo!')
    return HttpResponse(u'Hola mundo 2!')
