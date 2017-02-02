#!/usr/bin/python
# coding: utf-8
import smtplib
from email.mime.text import MIMEText
# Python 对 SMTP 支持有 smtplib 和 email 两个模块, email 负责构造邮件, smtplib 负责发送邮件
_user, _pwd, _to = "jia_ruipeng@qq.com", "mdzanakkorpsbid", "upc_jrp@163.com"  # pwd 是 授权码, 不是密码
# _user, _pwd, _to = "jia_ruipeng@qq.com", "mdzanakkorpsbidj", "1683751393@qq.com"
# qq邮箱, 点击: 设置 -> 账户 -> 找到 POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV 服务 -> 开启 IMAP/SMTP 服务 -> 手机发送到指定号码, 获取授权码

# msg = MIMEText(u"乔装打扮, 不择手段".encode('utf-8'))  # 中文的还没弄好, 以后再弄弄吧
msg = MIMEText("lalalalal")
msg["Subject"] = "don't panic"
msg["From"] = _user
msg["To"] = _to

s = smtplib.SMTP("smtp.qq.com", timeout=10)  # 连接 smtp 邮件服务器, 端口默认是 25, 最好设置一个 timeout, 否则出错后会卡住
s.set_debuglevel(1)  # 打印出和 SMTP 服务器交互的所有信息
s.starttls()  # 建立安全链接, SSL
s.login(_user, _pwd)  # 登陆服务器
s.sendmail(_user, _to, msg.as_string())  # 发送邮件
s.close()
# smtp.163.com, smtp.126.com, smtp.qq.com, smtp.gmail.com
# 另一种解决 SSL 问题的方法: s = smtplib.SMTP_SSL("smtp.qq.com", 465, timeout=10), 端口改为 465
