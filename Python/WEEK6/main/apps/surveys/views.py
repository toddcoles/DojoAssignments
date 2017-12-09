# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    return render(request, 'surveys/index.html')# render(request, "survey/index.html")

def result(request):
	if request.method == "POST":
		try:
			request.session['mycount']
		except KeyError:
			request.session['mycount'] = 0
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']
		request.session['mycount']  += 1
	return render(request, 'surveys/result.html')

def back(request):
	return redirect('/')