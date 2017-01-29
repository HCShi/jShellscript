#!/usr/bin/python
# coding: utf-8
"""Train tickets query via command-line.

Usage:
    jticket [-gdtkz] <from> <to> <date>

Options:
    -h,--help  显示帮助菜单
    -g         高铁
    -d         动车
    -t         特快
    -k         快速
    -z         直达

Example:
    jticket beijing shanghai 2016-08-25
"""
from docopt import docopt
import requests

def cli():
    arguments = docopt(__doc__)
    import os, json
    user_path = os.path.expanduser('~')
    f = open(user_path + '~/github/jKnowledge/info_gather/src/12306_dict'.lstrip('~'))
    stations = json.load(f)
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(
        date, from_station, to_station
    )
    print url
    # 呵呵, 烂尾了, 12306 不给玩了, 有时间再处理 403 吧
    # r = requests.get(url, verify=False)
    # print r.content
    # print r.json()

if __name__ == '__main__':
    cli()
