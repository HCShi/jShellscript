#!/usr/bin/python3
# coding: utf-8
# 1. session 保存 lt(token); 2. 密码要用 md5 加密过的; 3. 可以不用 headers; 4. 功能还没实现, 待完善
import requests, re, unicodedata
url = 'http://cas.upc.edu.cn/cas/login'
headers = {
    'Host': 'cas.upc.edu.cn',
    'Referer': 'http://cas.upc.edu.cn/cas/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'
}
s = requests.Session()
r = s.get(url)  # print r.text
ltt = re.findall('<input type="hidden" name="lt" value="(.*?)">', r.text, re.S)[0]
ltu = re.findall('(.*?)" />', ltt, re.S)[0]
lt = unicodedata.normalize('NFKD', ltu).encode('ascii','ignore')
# print lt
postData = {
    'encodedService': 'http%3a%2f%2fi.upc.edu.cn%2fdcp%2findex.jsp',
    'service': 'http://i.upc.edu.cn/dcp/index.jsp',
    'serviceName': 'null',
    'loginErrCnt': '0',
    'username': '12016222',
    'password': 'defac44447b57f152d14f30cea7a73cb',
    'lt': lt
}
# print postData

r = s.post(url, params = postData)
# print r.text
url_jwxt = re.findall('<a href="(.*?)">', r.text, re.S)[0]
url_jwxt = unicodedata.normalize('NFKD', url_jwxt).encode('ascii','ignore')
r = s.get(url_jwxt)
# print type(r)
# print r.text
url_jwxt = 'http://i.upc.edu.cn/dcp/forward.action?path=/portal/portal&p=home'
r = s.get(url_jwxt)
# print type(r)
# print r.text
# 居然重定向了两次才进去
# 上面已经进入了数字石大，下面开始重定向到教务系统,下面网址是通过在浏览器中进入数字石大后，在源代码中找到a href的属性标签得来得

url_jwxt = 'http://i.upc.edu.cn/dcp/forward.action?path=dcp/core/appstore/menu/jsp/redirect&appid=1180&ac=3'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)'
} # 一个IE的头，但是和不加差不多，都是无法创建对象
r = s.get(url_jwxt, headers = headers)
# print r.text
url_jwxt = 'http://211.87.177.1/jwxt/framework/new_window.jsp?lianjie=&winid=win2'
r = s.get(url_jwxt)
# print r.text # 得到了一个空的左右边栏，下面是点击成绩查询
# 从这里开始就不行了，下面的仅供参考

url_jwxt = 'http://211.87.177.1/jwxt/dwr/call/plaincall/dwrMonitor.emptyMap.dwr'
postData = {
    'callCount': '1page=/jwxt/framework/menuleft.jsp?fater=',
    'winid': 'win2httpSessionId=C0E60F1756A05E192572A7098C054573scriptSessionId=3CDADE8B1B8E2B7B1BE590D28D3A8B19767c0-scriptName=dwrMonitorc0-methodName=emptyMapc0-id=0c0-param0=string:query_xscj.jspCED39C310ADD0F8BE043C4E516ACA04EbatchId=0'
}
r = s.post(url_jwxt, params = postData)
# print r.text
# print type(r)
postData = {
    'kcmc': '',
    'kcxz': '',
    'kksj': '2015-2016-1',
    'ok': '',
    'xsfs': 'qbcj'
}

url_jwxt = 'http://211.87.177.1/jwxt/xszqcjglAction.do?method=queryxscj'
r = s.post(url_jwxt, params = postData)
print r.text
# print r.text
# r = s.get(url_jwxt)
# print r.text
