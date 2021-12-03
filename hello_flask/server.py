from flask import Flask, render_template
from flask.templating import render_template_string

app = Flask(__name__)

@app.route('/')
def landing_Page():
    return 'Pizza Parlor Dashboard: under construction go to "/dashboard"'

@app.route('/dashboard')
def dashboard():
    friend = "Pancakes"
    friends = ["Dante", "Nate", "Kev"]
    return render_template('dashboard.html', friend1 = friend, friends = friends)

@app.route('/dashboard/say/<string:name>')
def hiFlask(name):
    return ("hi " + name + "!")

@app.route('/dashboard/repeat/<string:num>/<string:word>')
def repeatYourself(num, word):
    return (word * int(num))


if __name__ == '__main__':
    app.run(debug=True)