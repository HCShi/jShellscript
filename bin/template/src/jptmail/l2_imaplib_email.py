# !/usr/bin/python
# coding: utf-8
import imaplib
import email
# 登陆邮箱
conn = imaplib.IMAP4_SSL(host='imap.qq.com', port='993')
conn.login('352111644@qq.com', 'mdzanakkorpsbidj')  # QQ 邮箱 IMAP/SMTP 授权码:
conn.select()

# 拉取邮件
type, data = conn.search(None, 'ALL')

# 打印邮件 data[0] 默认收件箱, 还没实现处理
for num in data[0].split():
    typ, data = conn.fetch(num, '(RFC822)')
    print ('Message %s\n%s\n' % (num, data[0][1].decode('utf-8')))
