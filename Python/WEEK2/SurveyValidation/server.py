from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
  error = False
  if len(request.form['name']) < 1:
    flash("Incorrect data length for name")
    error = True
  else:
    flash("Correct! Your name is {}".format(request.form['name']))
  
  if len(request.form['comment']) < 1:
    flash("Incorrect data length for comment")
    error = True
  elif len(request.form['comment']) > 120:
    flash("Data in comment should be less than 120 characters")
    error = True
  else:
    flash("Your comment is {}".format(request.form['comment']))

  session['info'] = request.form
  if error:
    return redirect('/')
    
  return redirect('/result')

@app.route('/result')
def correct_result():
  return render_template('result.html', result=session['info'])

app.run(debug=True)