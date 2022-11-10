from flask import Flask
from flask import render_template
from flask import request
import sqlite3 as sql

def addUser(username, email, password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Users (username, email, passwd) VALUES (?, ?, ?)", (username, email, password))
    con.commit()
    con.close()


def getUser(email):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Users WHERE email = ?", (email,))
    user = cur.fetchone()
    con.close()
    return user


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('signup.html')

@app.route('/user/signup', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        password = request.form['password']
        addUser(username, email, password)
        return render_template('signin.html')
    else:
        return render_template('signup.html')


@app.route('/user/signin', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = getUser(email)
        if user == None:
            return render_template('signin.html', error="Email or password is incorrect")
        elif user[3] == password:
            return render_template('welcome.html')
        else:
            return render_template('signin.html', error="Email or password is incorrect")
    else:
        return render_template('signin.html')


if __name__ == "__main__":
    app.run()