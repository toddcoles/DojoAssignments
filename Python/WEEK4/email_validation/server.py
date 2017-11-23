from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    # query = "SELECT id, email, DATE_FORMAT(created_at, '%m/%d/%y %l:%i %p') as created_at FROM emails"                           # define your query
    # emails = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html')                    # pass data to our template  -->, all_emails=emails


@app.route('/email', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    if EMAIL_REGEX.match(request.form['email']):
        query = "INSERT INTO emails (email, created_at) VALUES (:email, now())"
    # We'll then create a dictionary of data from the POST data received.
        data = {
                 'email': request.form['email']
                }
    # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        query2 = "SELECT id, email, DATE_FORMAT(created_at, '%m/%d/%y %l:%i %p') as created_at FROM emails"                           # define your query
        emails = mysql.query_db(query2) 
        current_email = request.form['email']
        return render_template('success.html', all_emails=emails, last_entry=emails[-1])
    return redirect('/wrong')

@app.route('/wrong')
def error_input():
    err_msg="Invalid email address"
    return render_template('index.html', message=err_msg)
# @app.route('/email/<email_id>')
# def show(email_id):
#     # Write query to select specific user by id. At every point where
#     # we want to insert data, we write ":" and variable name.
#     query = "SELECT * FROM emails WHERE id = :id"
#     # Then define a dictionary with key that matches :variable_name in query.
#     data = {'id': email_id}
#     # Run query with inserted data.
#     friends = mysql.query_db(query, data)
#     # Friends should be a list with a single object,
#     # so we pass the value at [0] to our template under alias one_friend.
#     return render_template('index.html', one_email=emails[0])


# @app.route('/update_friend/<friend_id>', methods=['POST'])
# def update(friend_id):
#     query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
#     data = {
#              'first_name': request.form['first_name'], 
#              'last_name':  request.form['last_name'],
#              'occupation': request.form['occupation'],
#              'id': friend_id
#            }
#     mysql.query_db(query, data)
#     return redirect('/')


@app.route('/delete/<email_id>')
def delete(email_id):
    query = "DELETE FROM emails WHERE id = :id"
    data = {'id': email_id}
    mysql.query_db(query, data)
    return redirect('success')

@app.route('/success')
def success():
    query2 = "SELECT id, email, DATE_FORMAT(created_at, '%m/%d/%y %l:%i %p') as created_at FROM emails"                           # define your query
    emails = mysql.query_db(query2) 
    return render_template('success.html', all_emails=emails, last_entry=emails[-1])

@app.route('/back')
def back():
    return redirect('/')

app.run(debug=True)