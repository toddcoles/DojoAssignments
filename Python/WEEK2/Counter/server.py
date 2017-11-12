from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisisSecret' #Secret key

@app.route('/')
def index():
  session['counter'] = session['counter'] + 1
  # session['counter'] = 0 #used to clear out the counter
  return render_template("index.html", counter=session['counter'])

@app.route('/increment', methods = ['POST'])
def increment():
  if request.form['mybutton'] == 'Erase':
    session['counter'] = 0
  elif request.form['mybutton'] == 'Add2':	
    session['counter'] = session['counter'] + 2
  # session['counter'] = 0 #used to clear out the counter
  return render_template("index.html", counter=session['counter'])

app.run(debug=True)