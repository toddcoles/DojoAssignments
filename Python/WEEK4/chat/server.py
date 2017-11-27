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
mysql = MySQLConnector(app, 'dojochat')

@app.route('/', methods=['GET'])
def index():
    insert_query2 = "SELECT m.id, m.user_id, m.message, DATE_FORMAT(m.created_at, '%M %D %Y %l:%i %p') as created_at, m.updated_at, CONCAT(u.first_name,' ',u.last_name) as name from messages as m JOIN users as u ON m.user_id = u.id GROUP BY message ORDER BY created_at DESC;"
    result2 = mysql.query_db(insert_query2)

    insert_query3 = "SELECT m.id, m.user_id, c.message_id, c.user_id, c.comment, DATE_FORMAT(c.created_at, '%M %D %Y %l:%i %p') as created_at, c.updated_at, CONCAT(u.first_name,' ',u.last_name) as name FROM messages as m LEFT JOIN comments as c ON m.id = c.message_id LEFT JOIN users as u ON u.id = c.user_id GROUP BY c.comment ORDER BY c.created_at DESC;"
    result3 = mysql.query_db(insert_query3)
            
    return render_template('index.html', all_users=result2, all_posts=result3) #, auth_user=user) # pass data to our template

@app.route('/create_user', methods=['POST'])
def create_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest();
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

    if (len(request.form['password']) < 8):
        flash("Passwords must be at least 8 characters", "password")
        error = True
    else:
        password = md5.new(request.form['password']).hexdigest();
        #pw_hash = bcrypt.generate_password_hash(password)
        #session['info'] = request.form
        #session['password'] = request.form['pw_hash']

    if error:
        return redirect('/')
    else:
        insert_query = "INSERT INTO users (first_name, last_name, created_at, updated_at, email, password) VALUES (:first_name, :last_name,  NOW(), NOW(), :email, :password)"
        query_data = { 'first_name': first_name, 'last_name': last_name, 'email': email,'password': password }
        result = mysql.query_db(insert_query, query_data)
        # session['status'] = request.form['username'] #User automatically logged on when they register with this line
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
    password = md5.new(request.form['password']).hexdigest();
    query = "SELECT * FROM users WHERE email = :email AND password = :password"                           # define your query
    data = {
             'email': request.form['email'], 
             'password':  password # // md5.new(request.form['pw_hash']).hexdigest();
           }
    user = mysql.query_db(query, data)
    if user:
        if (user[0]['email'] == request.form['email']) and (user[0]['password'] == password): # run query with query_db()
            session['status'] = user[0]['first_name']
            session['user_id'] = user[0]['id']
            user_id = session['user_id']

            insert_query2 = "SELECT m.id, m.user_id, m.message, DATE_FORMAT(m.created_at, '%M %D %Y %l:%i %p') as created_at, m.updated_at, CONCAT(u.first_name,' ',u.last_name) as name from messages as m JOIN users as u ON m.user_id = u.id GROUP BY message ORDER BY created_at DESC;"
            query_data2 = { 'user_id': user_id }
            result2 = mysql.query_db(insert_query2, query_data2)

            insert_query3 = "SELECT m.id, m.user_id, c.message_id, c.user_id, c.comment, DATE_FORMAT(c.created_at, '%M %D %Y %l:%i %p') as created_at, c.updated_at, CONCAT(u.first_name,' ',u.last_name) as name FROM messages as m LEFT JOIN comments as c ON m.id = c.message_id LEFT JOIN users as u ON u.id = c.user_id GROUP BY c.comment ORDER BY c.created_at DESC;"
            result3 = mysql.query_db(insert_query3)
            
            return render_template('index.html', all_users=result2, all_posts=result3) #, auth_user=user) # pass data to our template
        else:
            flash("ERROR: Username or password not in database", "user_err")
            error = True
            if error:
                return redirect('/login')
    else:
        return redirect('/')

@app.route('/delete/<user_id>')
def delete(user_id):
    query = "DELETE FROM users WHERE id = :id"
    data = {'id': user_id}
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/add_message', methods=['POST'])
def add_msg():
    user_id = session['user_id']
    msg = request.form['posts']
    insert_query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message,  NOW(), NOW())"
    query_data = { 'user_id': user_id, 'message': msg }
    result = mysql.query_db(insert_query, query_data)

    insert_query2 = "SELECT m.id, m.user_id, m.message, DATE_FORMAT(m.created_at, '%M %D %Y %l:%i %p') as created_at, m.updated_at, CONCAT(u.first_name,' ',u.last_name) as name from messages as m JOIN users as u ON m.user_id = u.id GROUP BY message ORDER BY created_at DESC;"
    query_data2 = { 'user_id': user_id }
    result2 = mysql.query_db(insert_query2, query_data2)

    insert_query3 = "SELECT m.id, m.user_id, c.message_id, c.user_id, c.comment, DATE_FORMAT(c.created_at, '%M %D %Y %l:%i %p') as created_at, c.updated_at, CONCAT(u.first_name,' ',u.last_name) as name FROM messages as m LEFT JOIN comments as c ON m.id = c.message_id LEFT JOIN users as u ON u.id = c.user_id GROUP BY c.comment ORDER BY c.created_at DESC;"
    result3 = mysql.query_db(insert_query3)
    return render_template('index.html', all_users=result2, all_posts=result3)

@app.route('/add_comment/<msg_id>', methods=['POST'])
def add_comment(msg_id):
    user_id = session['user_id']
    msg = request.form['add_comment']

    insert_query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:user_id, :message_id, :comment,  NOW(), NOW())"
    query_data = { 'user_id': user_id, 'message_id': msg_id, 'comment': msg }
    result = mysql.query_db(insert_query, query_data)

    insert_query2 = "SELECT m.id, m.user_id, m.message, DATE_FORMAT(m.created_at, '%M %D %Y %l:%i %p') as created_at, m.updated_at, CONCAT(u.first_name,' ',u.last_name) as name from messages as m JOIN users as u ON m.user_id = u.id GROUP BY message ORDER BY created_at DESC;"
    query_data2 = { 'user_id': user_id }
    result2 = mysql.query_db(insert_query2, query_data2)

    insert_query3 = "SELECT m.id, m.user_id, c.message_id, c.user_id, c.comment, DATE_FORMAT(c.created_at, '%M %D %Y %l:%i %p') as created_at, c.updated_at, CONCAT(u.first_name,' ',u.last_name) as name FROM messages as m LEFT JOIN comments as c ON m.id = c.message_id LEFT JOIN users as u ON u.id = c.user_id GROUP BY c.comment ORDER BY c.created_at DESC;"
    result3 = mysql.query_db(insert_query3)
    return render_template('index.html', all_users=result2, all_posts=result3)

app.run(debug=True)