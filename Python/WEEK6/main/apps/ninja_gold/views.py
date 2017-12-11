from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, "ninja_gold/index.html")

def process_money(request):
    time = datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
    # print time
    building = request.POST['building'] ## this was changed from Flask
    if building == 'farm':
        gold = random.randrange(10,20+1)
        request.session['activities'].append({'activity':"You entered a {} and earned {} golds".format(building, gold), 'class':'win', 'date':time})

    elif building == 'cave':
        gold = random.randrange(5,10+1)
        request.session['activities'].append({'activity': "You entered a {} and earned {} golds".format(building, gold), 'class':'win', 'date':time})

    elif building == 'house':
        gold = random.randrange(2,5+1)
        request.session['activities'].append({'activity': "You entered a {} and earned {} golds".format(building, gold), 'class':'win', 'date':time})

    elif building == 'casino':
        gold = random.randrange(-50,50+1)
        if gold < 0:
            request.session['activities'].append({'activity': "You entered a {} and lost {} golds".format(building, gold), 'class': 'loss', 'date':time})
        else:
            request.session['activities'].append({'activity': "You entered a {} and earned {} golds".format(building, gold), 'class':'win', 'date':time})

    request.session['gold'] += gold
    return redirect('/')