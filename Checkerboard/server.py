from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/')       
def index():
    return render_template("index.html", width=8, height=8, color1="blue", color2="grey")

@app.route('/<int:height>')       
def changeHeight(height):
    return render_template("index.html", width=8, height=height, color1="blue", color2="grey")

@app.route('/play/<string:color1>/<string:color2>/<int:width>/<int:height>')
def changeDiminsionsandColors(color1, color2, width, height):
    return render_template("index.html", color2=color2, color1=color1, width=width, height=height)

@app.errorhandler(404)
def check(error):
    return f"page not found"

if __name__=="__main__":   
    app.run(debug=True)   