#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render


def hello(request):
	context = {}
	context['lk'] = '刘可'
	context['zf'] = '张帆'
	context['lzy'] = '刘兆祎'
	return render(request, 'hello.html', context)