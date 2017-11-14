# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    error = False
    #CHECKING VALIDATION OF EMAIL
    if len(request.form['email']) == 0:
      flash("Email cannot be blank!")
      error = True
    elif not EMAIL_REGEX.match(request.form['email']):
      flash("Invalid Email Address!")
      error = True
    elif not EMAIL_REGEX.match(request.form['email']):
      flash("Invalid Email Address!")
      error = True
    else:
      flash("Success!")

    #CHECKING VALIDATION OF FIRST NAME
    if(len(request.form['first_name'])) == 0:
      flash("First name cannot be blank")
      error = True

    #CHECKING VALIDATION OF CHARACTERS IN FIRST AND LAST NAME
    if not (request.form['first_name']).isalpha():
      flash("First name must contain only letters")
      error = True
    if not (request.form['last_name']).isalpha():
      flash("Last name must contain only letters")
      error = True

    if request.form['password'] != request.form['confirm_password']:
      flash("Passwords do not match")
      error = True

    session['info'] = request.form
    session['password'] = 'valid'
    if error:
      return redirect('/')

    return redirect('/result')

@app.route('/result')
def correct_result():
  return render_template('result.html', result=session['info'], valid=session['password'])

app.run(debug=True)