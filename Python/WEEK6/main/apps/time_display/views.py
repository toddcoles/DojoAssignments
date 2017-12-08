# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
	context = {
	"mytime": strftime("%b %d, %Y %I:%M %p", gmtime())
	}  
	return render(request,'time_display/index.html', context)

# Create your views here.

