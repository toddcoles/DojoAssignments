# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, redirect

def index(request):
	return render(request, 'session_words/index.html')

def add_word(request):
	new_word = {}
	for key, value in request.POST.iteritems():
		# print key, value
		if key != "csrfmiddlewaretoken" and key != "show-big":
			new_word[key] = value
		if key == "big":
			new_word['big'] = "big"
		else:
			new_word['big'] = ""
	new_word['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
	try:
		request.session['words']
	except KeyError:
		request.session['words'] = []

	temp_list = request.session['words']
	temp_list.append(new_word)
	request.session['words'] = temp_list
	# for key, val in request.session.__dict__.iteritems():
	# 	print key, val
	# print "post created at", new_word

	return redirect('/')


def delete(request):
	for key in request.session.keys():
		del request.session[key]
	return redirect('/')