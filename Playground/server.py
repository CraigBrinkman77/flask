from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/')
@app.route('/<string:color>/<int:num>')
def create(color="blue", num=3):
    return render_template("index.html", color=color, num=num)

@app.errorhandler(404)
def check(error):
    return f"page not found"

if __name__=="__main__":   
    app.run(debug=True)    

