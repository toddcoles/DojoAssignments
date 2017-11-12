from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# Route to the index to display the form
@app.route('/')
def index():
  return render_template("index.html")

# This is the route to show the entered data
@app.route('/result', methods=['POST'])
def result():
   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   comment = request.form['comment']
   # redirects back to the '/' route
   return render_template('result.html', name=name, location=location, language=language, comment=comment)
app.run(debug=True)