# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect

def index(request):
	context = {
		"first_books": Review.objects.all()[:3],
		"all_books": Review.objects.all()[3:]
	}
	return render(request, 'review/index.html', context)

def add_review(request):
	context = {
		"authors": Author.objects.all()
	}
	return render(request, 'review/add.html', context)

def create(request):
	errs = Review.objects.validate_review(request.POST)
	if errs:
		for e in errs:
			messages.error(request, e)
	else:
		book_id = Review.objects.create_review(request.POST, request.session['user_id']).book.id
	return redirect('/review/show/{}'.format(book_id))

def show(request, book_id):
	context = {
		"mybook": Review.objects.last()
	}
	return render(request, 'review/show.html', context)

def user(request, user_id):
	context = {
		"myuser": User.objects.get(id=user_id),
		"user_reviews": Review.objects.all()
	}
	return render(request, 'review/user.html', context)
