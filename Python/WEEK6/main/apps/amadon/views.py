# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, redirect

items = [
	{
		"id": 1,
		"name": "Dojo T-Shirt",
		"price": 19.99,
	},
	{
		"id": 2,
		"name": "Dojo Sweater",
		"price": 29.99
	},
	{
		"id": 3,
		"name": "Dojo Cup",
		"price": 4.99
	},
	{
		"id": 4,
		"name": "Algorithm Book",
		"price": 49.99
	}
]

def index(request):
	context = {
		"items": items
	}
	return render(request, 'amadon/index.html', context)

def buy(request, item_id):
	# new_product = {}
	# for key, value in request.POST.iteritems():
	# 	# print key, value
	# 	if key != "csrfmiddlewaretoken":
	# 		new_product[key] = value
	# new_product['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
	# try:
	# 	request.session['product']
	# except KeyError:
	# 	request.session['product'] = []

	# temp_list = request.session['product']
	# temp_list.append(new_product)
	# request.session['product'] = temp_list
	# for key, val in request.session.__dict__.iteritems():
	# 	print key, val
	# print "post created at", new_word
	for item in items:
		if item['id'] == int(item_id):
			amount_charged = item['price'] * int(request.POST['quantity'])

	# handle exceptions for session keys if they do not yet exist
	try:
		request.session['total_charged']
	except KeyError:
		request.session['total_charged'] = 0

	try:
		request.session['total_items']
	except KeyError:
		request.session['total_items'] = 0        

	request.session['total_charged'] += amount_charged
	request.session['total_items'] += int(request.POST['quantity'])
	request.session['last_transaction'] = amount_charged
	
	return redirect('/checkout')


def checkout(request):
	# for key in request.session.keys():
		# del request.session[key]
	return render(request, 'amadon/checkout.html')

def clear(request):
	for key in request.session.keys():
		del request.session[key]
	return redirect('/')