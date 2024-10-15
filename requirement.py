from flask import Flask, request, render_template, url_for, jsonify

app = Flask(__name__)

TOKEN = "SecretToken"
todos = []

#R2
@app.route('/')
def home():
    return render_template('R2/index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form["username"]
    mail = request.form["u_email"]
    age = request.form["Age"]

    return render_template('R2/result.html',
                           username=username,
                           mail=mail,
                           age=age)

if __name__=='__main__':
    app.run(debug=True)