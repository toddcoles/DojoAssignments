# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.messages import error
from django.shortcuts import render, redirect
from models import *

def index(request):
	context = {
	"items": course.objects.all()
	}
	return render(request, 'course/index.html', context)

def add_course(request):
	errors = course.objects.validate(request.POST)
	if errors:
		for err in errors:
			error(request, err)
	else:
		course.objects.create(
			course_name=request.POST['course_name'],
			desc=request.POST['desc']
		)
	return redirect('/')

def delete(request, course_id):
	course.objects.get(id=course_id).delete()
	return redirect('/')