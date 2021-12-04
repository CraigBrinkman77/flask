from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
import random
app.secret_key = "jhgfsejkhdgfkjhs dbj"

@app.route('/')       
def index():
    return render_template("index.html")

@app.post('/guess')
def checkCorrect():
    session['random_number'] = random.randint(0,100)
    session['guess'] = int(request.form['guess'])
    session['guess'] > session['random_number']
    print (session['random_number'])

    return redirect('/')

@app.errorhandler(404)
def check(error):
    return f"page not found"

if __name__=="__main__":   
    app.run(debug=True) 