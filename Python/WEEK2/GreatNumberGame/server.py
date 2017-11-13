from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisisSecret' #Secret key

@app.route('/')
def index():
  # if 'number' not in session:
  session['number'] = random.randrange(0,101)
  session['message'] = ""
  session['guess'] = ""
  session['class'] = ""
  # session['counter'] = 0 #used to clear out the counter
  return render_template("index.html", Number=session['number'])

@app.route('/guess', methods = ['POST'])
def guess():
  session['guess'] = int(request.form['mynum'])
  if session['number'] > int(request.form['mynum']):
    session['message'] = "Number too low!"
    session['class'] = "low"
  elif session['number'] < int(request.form['mynum']):
  	session['message'] = "Number too high!"
  	session['class'] = "high"
  else:
    session['message'] = "That is correct! Play again!!"
    return redirect('/reset')
    session['class'] = "correct"

  return render_template("index.html", guess=session['guess'], message=session['message'], Number=session['number'], cssClass=session['class'])

@app.route('/reset')
def reset():
  session['message'] = "Play again!"
  # session.pop('number')
  # session.pop('message')
  return render_template('result.html', message=session['message'])

@app.route('/restart', methods=['POST'])
def restart():
  return redirect('/')

app.run(debug=True)