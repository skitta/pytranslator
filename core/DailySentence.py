#!/usr/env/python3
# -*-coding:utf-8-*-

"""
documentary
"""

import re
from urllib import request

__author__ = 'skitta'


def get_sentence():
    try:
        url = 'http://news.iciba.com/dailysentence/'
        html = request.urlopen(url).read().decode()
    except Exception as error:
        return
    else:
        patten = re.compile(r'<a target="_blank" href=.*?detail.*?</a>')
        en = patten.findall(html)[2].split('>')[1].split('<')[0]
        zh = patten.findall(html)[3].split('>')[1].split('<')[0]
        config_str = '\n%s\n\n%s' % (en, zh)
        return config_str


if __name__ == '__main__':
    print(get_sentence())