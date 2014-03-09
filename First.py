# -*- coding: utf-8 -*-
'''
第一個練習，簡單的網頁連結
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="/hello">index page!</a><br>' \
    + '<a href="/hello">hello world page!</a><br>' \
    + '<a href="/hello/ASDF">string hello world page!</a><br>' \
    + '<a href="/hello/123">int hello world page!</a><br>' \
    + '<a href="/hello/1.344">float hello world page!</a><br>'

@app.route('/hello')
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

# @app.route('/asdf/')
# def show_test():
#		'''接受/asdf和/asdf/'''
#     return 'test'

# @app.route('/asdf')
# def show_test3():
#		'''不接受/asdf/'''
#     return 'test1'


if __name__ == '__main__':
    app.run(debug=True)    


