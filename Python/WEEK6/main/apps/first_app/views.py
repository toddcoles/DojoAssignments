# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
	response = "Hello, I am your first and second request"
	return HttpResponse(response)
# Create your views here.
