from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 

@app.route('/')       
def index():
    return render_template("index.html", color="blue", num=3)

@app.errorhandler(404)
def check(error):
    return f"page not found"

if __name__=="__main__":   
    app.run(debug=True) 