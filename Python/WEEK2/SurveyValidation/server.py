from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
  if len(request.form['name']) < 1:
    flash("Incorrect data length for name")
    return redirect('/')
  else:
    flash("Correct! Your name is {}".format(request.form['name']))
  
  if len(request.form['comment']) < 1:
    flash("Incorrect data length for comment")
    return redirect('/')
  elif len(request.form['comment']) > 120:
    flash("Data in comment should be less than 120 characters")
    return redirect('/')
  else:
    flash("Your comment is {}".format(request.form['comment']))

  session['info'] = request.form
  return redirect('/result')

@app.route('/result')
def correct_result():
  return render_template('result.html', result=session['info'])

app.run(debug=True)