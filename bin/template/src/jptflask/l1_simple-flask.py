#!/usr/bin/python3
# coding: utf-8
from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])                      # GET /: 首页, 返回Home
def home():
    return '<h1>Home</h1>'
@app.route('/signin', methods=['GET'])                        # GET /signin: 登录页, 显示登录表单
def signin_form():
    return '''<form action="/signin" method="post">
                <p><input name="username"></p>
                <p><input name="password" type="password"></p>
                <p><button type="submit">Sign In</button></p>
              </form>'''
@app.route('/signin', methods=['POST'])                       # POST /signin: 处理登录表单, 显示登录结果
def signin():  # Flask 通过 request.form['name'] 来获取表单的内容
    if request.form['username'] == 'admin' and request.form['password'] == 'password':  # 需要从 request 对象读取表单内容
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'
if __name__ == '__main__':
    app.run()
