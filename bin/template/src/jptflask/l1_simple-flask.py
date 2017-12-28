#!/usr/bin/python3
# coding: utf-8
from flask import Flask, url_for, request
app = Flask(__name__)
##################################################################
## 简单操作
## 根路径
@app.route('/', methods=['GET', 'POST'])  # GET /: 首页, 返回 Home
def home(): return '<h1>Home</h1>'  # jcurl 5000
## 变量: string, int, float, path, any, uuid
@app.route('/user/<username>')
def profile(username): return 'User %s' % username  # jcurl 5000 user/jia
## 整形
@app.route('/post/<int:post_id>')
def post(post_id): return 'Post %d' % post_id  # jcurl 5000 post/23
## HTTP Methods: GET, HEAD, POST, PUT, DELETE, OPTIONS
@app.route('/http', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': return '{"type": "Post"}'  # jcurl -p 5000 http
    else: return '{"type": "Get"}'                          # jcurl 5000 http

with app.test_request_context():  # 这里直接执行 python filename.py 也能输出
    print(url_for('home'))  # /;                                         要使用函数名
    print(url_for('home', next='/'))  # /?next=%2F;                      Unknown variable parts are appended to the URL as query parameters
    print(url_for('profile', username='John Doe'))  # /user/John%20Doe;  each corresponding to the variable part of the URL rule
    print(url_for('post', post_id=3))  # /post/3
##################################################################
## 下面是复杂的处理
@app.route('/signin', methods=['GET'])    # GET /signin: 登录页, 显示登录表单
def signin_form():
    return '''<form action="/signin" method="post">
                <p><input name="username"></p>
                <p><input name="password" type="password"></p>
                <p><button type="submit">Sign In</button></p>
              </form>'''
@app.route('/signin', methods=['POST'])   # POST /signin: 处理登录表单, 显示登录结果
def signin():  # Flask 通过 request.form['name'] 来获取表单的内容
    if request.form['username'] == 'admin' and request.form['password'] == 'password':  # 需要从 request 对象读取表单内容
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

##################################################################
## 这里加上 app.run() 后就能直接 python filename.py 开启服务器了, 但是最新版本不推荐
if __name__ == '__main__':
    app.run()
