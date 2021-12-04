from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = "hjvaefjhvgsjhfd"
@app.route('/')       
def index():
    if 'your_gold' not in session:
        session['your_gold'] = 0
    return render_template("index.html")

@app.route('/play', methods= ["POST"])
def play():
    if request.form['location'] == 'farm':
        session['your_gold'] += 15
    if request.form['location'] == 'cave':
        session['your_gold'] += 10
    if request.form['location'] == 'house':
        session['your_gold'] += 18
    if request.form['location'] == 'dice':
        session['your_gold'] += 20

    # print(session['action_farm'])
    return redirect('/')







@app.errorhandler(404)
def check(error):
    return f"page not found"

if __name__=="__main__":   
    app.run(debug=True) 