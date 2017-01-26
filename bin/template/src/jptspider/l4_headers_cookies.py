#!/usr/bin/python
# coding: utf-8
import requests
url = 'http://i.baidu.com/'  # 测试百度用户界面
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
cookie = {"Cookie": "BAIDUID=78D17BD56E419ADBBD86E06851FC68E5:FG=1; BDUSS=J6S1NldGtxT2xRWXNGR2NKVDBhUFNadmkwflV6M1JFUWR0TWd-bVE4ajUzWjlZSVFBQUFBJCQAAAAAAAAAAAEAAADYALkrsK7O0tbQu6rQobvsu-wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPlQeFj5UHhYdV; locale=zh; BIDUPSID=78D17BD56E419ADBBD86E06851FC68E5; PSTM=1484313385; pgv_pvi=1525854208; cflag=15%3A3; PSINO=5; H_PS_PSSID=1469_21112_19898_21614; PHPSESSID=05h69ap7argejrhgpabkgii9v1; Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04=1484886505; Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04=1484886505"}
print requests.get(url, cookies=cookie, headers=header, verify=False).content
# 添加 verify=False 参数不验证证书, 对 12306 很管用
