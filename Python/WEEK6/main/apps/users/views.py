# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display all the list of users")

def register(request):
	return HttpResponse("placeholder to display all users created")

def users(request):
	return HttpResponse("Placeholder to later display all the list of users")

def login(request):
	return HttpResponse("Placeholder for users to login")