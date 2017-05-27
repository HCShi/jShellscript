#!/usr/bin/python
# coding: utf-8
import requests
##################################################################
## httpbin, 常用的网站
url = 'http://httpbin.org/get'
print(requests.get(url).content)
# 通常我们比较关注其中的 User-Agent 和 Accept-Encoding
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch'
}
# headers = {'User-Agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate, sdch'}  # 短点也行
print(requests.get(url, headers = headers).content)
##################################################################
## 测试百度用户界面, 要先登录一下, 然后将 cookie 替换下面的
url = 'http://i.baidu.com/'
header = {
    'Host': 'i.baidu.com',
    'Referer': 'http://cas.upc.edu.cn/cas/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'
}
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
cookie = {"Cookie": "BAIDUID=78D17BD56E419ADBBD86E06851FC68E5:FG=1; BDUSS=J6S1NldGtxT2xRWXNGR2NKVDBhUFNadmkwflV6M1JFUWR0TWd-bVE4ajUzWjlZSVFBQUFBJCQAAAAAAAAAAAEAAADYALkrsK7O0tbQu6rQobvsu-wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPlQeFj5UHhYdV; locale=zh; BIDUPSID=78D17BD56E419ADBBD86E06851FC68E5; PSTM=1484313385; pgv_pvi=1525854208; cflag=15%3A3; PSINO=5; H_PS_PSSID=1469_21112_19898_21614; PHPSESSID=05h69ap7argejrhgpabkgii9v1; Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04=1484886505; Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04=1484886505"}
print(requests.get(url, cookies=cookie, headers=header, verify=False).content)
# 添加 verify=False 参数不验证证书, 对 12306 很管用
##################################################################
## params; UPC 联网登录账号
url = 'http://222.195.191.230:801/eportal/?c=ACSetting&a=Login&wlanuserip=null&wlanacip=null&wlanacname=null&port=&iTermType=1&session=null'
postData = {
    'DDDDD': '12016222@upc',
    'upass': '12345679',
    'R1': '0',
    'R2': '',
    'R6': '0',
    'para': '00',
    '0MKKey': '123456'
} # 这是宿舍的 postData, 用户名后面要加 @upc, url 的 ip 地址可能不同
s = requests.session()
r = s.post(url, params = postData); print r.text
##################################################################
## proxies, 维护一个代理 IP 池, 网上有很多免费的代理 IP, 可以通过筛选找到能用的; 解决由于 "频繁点击" 而需要输入验证码登陆的情况
# proxies = {'http': 'http://XX.XX.XX.XX:XXXX'}
# response = requests.get(url=url, proxies=proxies)
