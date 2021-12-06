from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = "ysgfjygfde"

@app.route('/')       
def index():
    session.clear()
    return render_template("index.html")

@app.post('/process')       
def process():
    session['name'] = request.form['name']
    session['city'] = request.form['city'] 
    session['language'] = request.form['language']  
    session['comment'] = request.form['comment'] 
    return redirect('/result')

@app.route('/result')       
def result():
    return render_template("result.html")


@app.errorhandler(404)
def check(error):
    return f"page not found"

if __name__=="__main__":   
    app.run(debug=True) 
