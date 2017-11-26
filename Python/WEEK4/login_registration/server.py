from flask import Flask, request, render_template, redirect, session, flash
from mysqlconnection import MySQLConnector
# imports the Bcrypt module
from flask_bcrypt import Bcrypt
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = "TColes secret_key"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'friendsdb')

    # this will load a page that has 2 forms one for registration and login
    #First Name - letters only, at least 2 characters and that it was submitted
    #Last Name - letters only, at least 2 characters and that it was submitted
    #Email - Valid Email format, and that it was submitted
    #Password - at least 8 characters, and that it was submitted
    #Password Confirmation - matches password

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html') #, all_users=all_users_query)
# we are going to add functions to create new users and login users

@app.route('/create_user', methods=['POST'])
def create_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    username = request.form['username']
    pw_hash = md5.new(request.form['pw_hash']).hexdigest();
    error = False
 # run validations and if they are successful we can create the password hash with bcrypt
 # now we insert the new user into the database
    #CHECKING VALIDATION OF EMAIL
    if len(request.form['email']) == 0:
        flash("Email cannot be blank!", "email")
        error = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", "email")
        error = True
 # else:
 #   flash("Success!")

    #CHECKING VALIDATION OF FIRST NAME
    if(len(request.form['first_name'])) < 2:
        flash("First name must be more than two characters", "name")
        error = True
    if(len(request.form['last_name'])) < 2:
        flash("Last name must be more than two characters", "name")
        error = True
    #CHECKING VALIDATION OF CHARACTERS IN FIRST AND LAST NAME
    if not (request.form['first_name']).isalpha():
        flash("First name must contain only letters", "name")
        error = True
    if not (request.form['last_name']).isalpha():
        flash("Last name must contain only letters", "name")
        error = True

    if (len(request.form['pw_hash']) < 8):
        flash("Passwords must be at least 8 characters", "password")
        error = True
    else:
        pw_hash = md5.new(request.form['pw_hash']).hexdigest();
        #pw_hash = bcrypt.generate_password_hash(password)
        #session['info'] = request.form
        #session['password'] = request.form['pw_hash']

    if error:
        return redirect('/')
    else:
        insert_query = "INSERT INTO friends (first_name, last_name, created_at, updated_at, email, pw_hash, username) VALUES (:first_name, :last_name,  NOW(), NOW(), :email, :pw_hash, :username)"
        query_data = { 'first_name': first_name, 'last_name': last_name, 'email': email,'pw_hash': pw_hash, 'username': username }
        result = mysql.query_db(insert_query, query_data)
        session['status'] = request.form['username']
 # redirect to success page
        return redirect('/')

@app.route('/result')
def correct_result():

    return render_template('result.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
 
@app.route('/register')
def register_user():
    return render_template('/register.html')

@app.route('/login')
def login():
    return render_template('/login.html')

@app.route('/login_user', methods=['POST'])
def login_user():
    error = False
    pw_hash = md5.new(request.form['pw_hash']).hexdigest();
    query = "SELECT id, username, pw_hash FROM friends WHERE username = :username AND pw_hash = :pw_hash"                           # define your query
    data = {
             'username': request.form['username'], 
             'pw_hash':  pw_hash # // md5.new(request.form['pw_hash']).hexdigest();
           }
    user = mysql.query_db(query, data)
    if user:
        if (user[0]['username'] == request.form['username']) and (user[0]['pw_hash'] == pw_hash): # run query with query_db()
            session['status'] = user[0]['username']
            return render_template('index.html') #, auth_user=user) # pass data to our template
        else:
            flash("ERROR: Username or password not in database", "user_err")
            error = True
            if error:
                return redirect('/login')
    else:
        return redirect('/login')

app.run(debug=True)