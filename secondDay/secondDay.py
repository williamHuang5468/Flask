# -*- coding: utf-8 -*-
'''
第二個練習，簡單的網頁連結
'''
from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')
def index(): 
	url_for('static', filename='style.css')
	return '<a href="/user/secondDay">secondDay</a><br>' \
		+ '<a href="/login">login</a>' \
		+ '<h1>style test</h1>'

@app.route('/user/<username>')
def profile(username):
	return 'this is %s' % username

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		do_the_login()
	else:
		do_the_login()

if __name__ == '__main__':
    app.run(debug=True)