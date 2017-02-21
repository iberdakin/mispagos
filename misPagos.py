#!/usr/bin/python
from flask import Flask, render_template, request
from listAllUsers import list_users

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/listusers/')   
def userslist():
	rows = list_users()
	return render_template('listusers.html',rows=rows)
   
if __name__ == '__main__':
   app.run(debug=True)