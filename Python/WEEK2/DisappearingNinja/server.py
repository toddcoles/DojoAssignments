from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/ninjas')
def show_ninjas():
  turtle = ['/static/leonardo.jpg', '/static/michelangelo.jpg', '/static/raphael.jpg', '/static/donatello.jpg']
  return render_template('ninjas.html', turtle=turtle)

@app.route('/ninjas/<color>')
def show_user_profile(color):
  theColors = ['blue', 'orange', 'red', 'purple']
  if color == 'blue':
    turtle = '/static/leonardo.jpg'
  elif color == 'orange':
    turtle = '/static/michelangelo.jpg'
  elif color == 'red':
    turtle = '/static/raphael.jpg'
  elif color == 'purple':
    turtle = '/static/donatello.jpg'
  elif color not in theColors:
    turtle = '/static/notapril.jpg'
  return render_template("ninjas.html", color=color, turtle=turtle)

@app.route('/route/with/<vararg>')
def handler_function(vararg):
  # here you can use the variable "vararg"
  # if you want to see what our argument looks like
  print vararg
  # we could do other things with this information from this point on such as:
  # use it to retrieve some records from the database
  # render a particular template

app.run(debug=True)
#*********************************************************************
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja/<color>')
def show(color):
    ninjas = {
        'orange':'michelangelo',
        'blue':'leonardo',
        'red':'raphael',
        'purple':'donatello'
    }
    
    if color in ninjas:
        character = ninjas[color]
    else:
        character = 'notapril'
    return render_template('show.html', character=character)

app.run(debug=True)