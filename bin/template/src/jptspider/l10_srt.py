#!/usr/bin/python3
# coding: utf-8
# 可以先用 ffmpeg 将其它文件转换为 srt
# f = open('./tmp.srt')
srt_text = '''\
1
00:00:12,815 --> 00:00:14,509
Hello, world.

2
00:00:14,815 --> 00:00:16,498
Hello, Jia Ruipeng

3
00:00:16,934 --> 00:00:17,814
Hello, UCAS
'''  # open('./tmp.srt').read()
##################################################################
## 手动处理
sections = srt_text.split('\n\n')  # 每三行一个空行, 进行分割
print(len(sections))  # 3
results = [[item for item in section.split('\n')] for section in sections]
print(results[0][1].split(' ')[0].split(',')[0])  # 00:00:12

##################################################################
## srt 库
import srt, pprint
gen = list(srt.parse(srt_text)); print(type(gen))
pprint.pprint(gen)
# [Subtitle(index=1, start=datetime.timedelta(0, 12, 815000), end=datetime.timedelta(0, 14, 509000), content='Hello, world.', proprietary=''),
#  Subtitle(index=2, start=datetime.timedelta(0, 14, 815000), end=datetime.timedelta(0, 16, 498000), content='Hello, Jia Ruipeng', proprietary=''),
#  Subtitle(index=3, start=datetime.timedelta(0, 16, 934000), end=datetime.timedelta(0, 17, 814000), content='Hello, UCAS', proprietary='')]
print(type(gen[0])) # <class 'srt.Subtitle'>
sub_1 = gen[0]
print(sub_1.start)  # 0:00:12.815000
print(sub_1.end)  # 0:00:14.509000
print(sub_1.index)  # 1
print(sub_1.content)  # Hello, world.
print(sub_1.to_srt)
