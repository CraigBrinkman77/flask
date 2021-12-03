from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "sdsd"

@app.route('/')       
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template("index.html")

@app.route('/count')
def addToCounter():
    session['count'] += 1 
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect('/')


@app.errorhandler(404)
def check(error):
    return f"page not found"

if __name__=="__main__":   
    app.run(debug=True) 