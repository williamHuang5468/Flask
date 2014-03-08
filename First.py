# -*- coding: utf-8 -*-
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="#">index page!</a>'

@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('hello.html', name=name)

# 傳入參數
@app.route('/hello/<username>')
def show_user_profile(username):
    return 'User %s' % username

# 傳入參數帶入型態，不符合型態就失敗
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'post %s' % post_id

@app.route('/post/<float:var>')
def show_float(var):
    return 'float %s' % var

if __name__ == '__main__':
    app.run(debug=True)    


