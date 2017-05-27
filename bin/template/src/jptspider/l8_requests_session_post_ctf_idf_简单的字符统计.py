#!/usr/bin/python
# coding: utf-8
"""
<html>
	<head>
		<title>字符统计</title>
	</head>
	<body>
		<b>请听题：</b>给你2秒钟的时间，告诉我下面这坨字符中有多少个w，多少个o，多少个l，多少个d和多少个y。
			把这些数字串成一个字符串提交一下就可以了，很简单吧~
		<hr />
			-n)wwN3o3X1no`HE*{BWx##o0PH02l20QqV=ncB&YHn*[*MSG0$e%Z`XX3pN=J6d_:s94L?Iw]P0#1x},[`cI7)1i}UhcP@:K;.mVs&7v58EE;v%x:V6pZI`}tini{G)1*Edd66h!&#zFy:H0aPp0.sgVOqVa9g?~y$.U?(vCh|Tk`K&pr.[^jRxZQi~rHxXyHV^?w``7)s~FMUOW_(ZY(TOrFnB)vM ,0%GLfQYa~ $8SUN (m|EO@aDf!rL[g{^zE7%tuA5A8WwS(@n(4j6B,Ls=-#sNc?r])~vPC~sDpoWo3&bHbBcF9Af1J$ 4lCVnP@Adba(*R^Tt[){^#?^kTn{;5($Sb b0|%`Z{4x[~j4^?j}~mntw[/Rp~Pg ZGr0I|Y|dz}7C^m-[gHbYMG8L|Akk/Xq7Nd4A[oRH%aCA rU2w:5;-t+:Z4@:;Hm=N*/F+iypXL2%nMEJj8cSFB5b{JVN.=m$w6h/Vcm-h6icSDh5(8H)#iCm!?.,eqN@y[O2H4wP!/{=Z@s3X1gVLa~|crN80AY{*+m}Gr.~?@jC7^f69K^{_TxoP9g:gmJt.G&@`lj1h/34SqgF%YC[4,6592g*O.!&.=N!3%u|h7/&ESpB/X}1m8w!o5rsi) vWMp*,sfqqY?RjKBi+pqmwx{]^HuOnDyRqjK1mw!Um,a+YW&n&k%V4W7qE.(l~#W/puWel(HV4n=9)cyG;/r3(El{V!K.o?ae|tpXb.U{s=I~B~$1,,}?.DN^f!.|=IYmkgx[rDDq#BqL(9m#k&gQwUe,/-|yXT ndgaOJl?;gb{${uK:yiA|W&,7s[urnEqbZs+}rAOC3r7T.+6aZE#QB8C,:L@d?W4X[/yi}J*GiWu1lc33e#Spfm$LOw$_o3mzfx;YX!zxf(Cw@SZhW{aAu(#WDgIN#nW2%]m8lr]]mCy2-m_]y0$_jT9]o,}*`.ilaH Be~xI-&BwAdSiH9ix2o5G*HyZK,mFEs}vI`,wLBG&qwro%1l7}[pipP{f4/#qk
		<hr />
		<form action="" method="post">
  			<p>答案: <input type="text" name="anwser" /></p>
  			<input type="submit" value="走你！" />
		</form>
	</body>
</html>
"""
import requests
url = "http://ctf.idf.cn/game/pro/37/"
s = requests.session()
res = s.get(url)
test = res.text.split('<hr />')
w, o, l, d, y = 0, 0, 0, 0, 0
for ch in test[1]:  # 两个 <hr /> 不是标签, 所以不好用 BeautifulSoup, 正好可以用 split
    if ch == "w": w += 1
    elif ch == "o": o += 1
    elif ch == "l": l += 1
    elif ch == "d": d += 1
    elif ch == "y": y += 1
answer = '%d%d%d%d%d' % (w, o, l, d, y)  # 也可以用 str(w) + str(o)
values = {'anwser': answer}
result = s.post(url, values)
"""
<form action="" method="post">
	<p>答案: <input type="text" name="anwser" /></p>
	<input type="submit" value="走你！" />
</form>
"""
print((result.text))
