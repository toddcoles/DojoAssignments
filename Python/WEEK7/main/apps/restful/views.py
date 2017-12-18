# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import *

def index(request):
	context = {
	"items": User.objects.all()
	}
	return render(request, 'restful/index.html', context)

def add_user(request):
	return render(request, 'restful/add_user.html')

def add_person(request):
	person = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
	person.save()
	return redirect('/')

def edit(request, user_id):
	context = {
		'user': User.objects.get(id=user_id)
		}
	return render(request, 'restful/update.html', context)

def delete(request, user_id):
	User.objects.get(id=user_id).delete()
	return redirect('/')

def update(request, user_id):

	user_to_update = User.objects.get(id=user_id)
	user_to_update.first_name = request.POST['first_name']
	user_to_update.last_name = request.POST['last_name']
	user_to_update.email = request.POST['email']
	user_to_update.save()
	return redirect('/')

def show(request, user_id):
	context = {
		'user': User.objects.get(id=user_id)
	}
	return render(request, 'restful/show.html', context)