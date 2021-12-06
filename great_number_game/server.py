
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
import random
app.secret_key = "jhgfsejkhdgfkjhs dbj"

@app.route('/')       
def index():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1
    if session['count'] > 5:
        session.clear()
        print('you loose')
    if 'random_number' not in session:
        session['random_number'] = random.randint(0,100)
    return render_template("index.html")

@app.post('/guess')
def checkCorrect():
    session['guess'] =  int(request.form['guess'])
    print (f"Guess: {session['guess']} Answer: {session['random_number']}")
    
    if session['guess'] > session['random_number']:
        print ('too high')
    if session['guess'] < session['random_number']:
        print ('too low')
    if session['guess'] == session['random_number']:
        print('correct')
        session.clear()
    
    return redirect('/')

@app.errorhandler(404)
def check(error):
    return f"page not found"

if __name__=="__main__":   
    app.run(debug=True) 