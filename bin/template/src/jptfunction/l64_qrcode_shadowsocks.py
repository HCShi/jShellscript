#!/usr/bin/python3
# coding: utf-8
import qrcode
##################################################################
## 1. 简单用法
img = qrcode.make('hello, qrcode')
img.save('tmp.png')
##################################################################
## 2. 高级用法
qrcode.data_list = []
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('hello, qrcode')
qr.make(fit=True)
img = qr.make_image()
img.save('tmp-1.png')
# 参数讲解
# version: 值为 1~40 的整数, 控制二维码的大小(最小值是 1, 是个 12×12 的矩阵). 如果想让程序自动确定, 将值设置为 None 并使用 fit 参数即可.
# error_correction: 控制二维码的错误纠正功能. 可取值下列 4 个常量.
# 　　ERROR_CORRECT_L: 大约 7% 或更少的错误能被纠正.
# 　　ERROR_CORRECT_M (默认) : 大约 15% 或更少的错误能被纠正.
# 　　ROR_CORRECT_H: 大约 30% 或更少的错误能被纠正.
# box_size: 控制二维码中每个小格子包含的像素数.
# border: 控制边框 (二维码与图片边界的距离) 包含的格子数 (默认为 4, 是相关标准规定的最小值)
##################################################################
## 3. 生成 shadowsocks 二维码
import json, base64, sys
config = json.load(open('./shadowsocks.go.json'))
print(config['server'])
method, password, server, server_port = config['method'], config['password'], config['server'], config['server_port']
## 加密二维码的源码
raw_str = (method + ':' + password + '@' + server + ':' + str(server_port)).encode(); print(raw_str)
encodestr = base64.b64encode(raw_str)  # 使用 base64 加密
shareqrcode_str = 'ss://' + encodestr.decode()  # 最前面加上 `ss://`, 如果手机识别 ss 协议的话会自动转到 shadowsocks 客户端
## 生成二维码, 这里设置的是固定格式
img = qrcode.make(shareqrcode_str)
img.save('qrcode.png')
##################################################################
## 总结
# 1. 不用显示引入 pillow 库
# 2. Shadowsocks 加密方法
#    ss://method:password@hostname:port  # plain URI
#    ss://aes-128-cfb:test@192.168.100.1:8888  # example
#    ss://YmYtY2ZiOnRlc3RAMTkyLjE2OC4xMDAuMTo4ODg4Cg  # the BASE64 encoded URI
