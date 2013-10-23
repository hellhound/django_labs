# -*- coding:utf-8 -*-
from django import forms

class Form(forms.Form):
    field_a = forms.CharField(label='Field A',
        required=False)
    field_b = forms.CharField(label='Field B',
        max_length=2)
    field_c = forms.EmailField(label='Field C')
    field_d = forms.IntegerField(label='Field D',
        max_value=100, min_value=0)
