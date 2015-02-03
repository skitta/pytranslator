#!/usr/env/python3
# -*-coding:utf-8-*-

"""
documentary
"""

import json
from urllib import request, parse

__author__ = 'skitta'


def translate(word, trans_from='auto', trans_to='auto'):
    api_key = 'efVWN2paqPC7xrIPklvfVk0l'
    url = 'http://openapi.baidu.com/public/2.0/translate/dict/simple?'
    body = {
        'client_id': api_key,
        'q': word,
        'from': trans_from,
        'to': trans_to}
    trans_url = url + parse.urlencode(body)
    try:
        res = request.urlopen(trans_url)
    except Exception as error:
        return "NetWork Error"
    else:
        json_data = json.loads(res.read().decode())
        data = json_data['data']['symbols'][0]

    if data:
        ph_str = ''
        if 'ph_zh' in data:
            if data['ph_zh'] is not None:
                ph_str += 'Ping Yin:[' + data['ph_zh'] + ']\n'
        if 'ph_en' in data:
            if data['ph_en'] is not None:
                ph_str += 'EN:[' + data['ph_en'] + ']\n'
        if 'ph_am' in data:
            if data['ph_am'] is not None:
                ph_str += 'AM:[' + data['ph_am'] + ']\n'

        mean_str = ''
        parts = data['parts']
        for i in parts:
            part = i['part']
            mean_str += (part + '\n')
            means = i['means']
            for n in means:
                mean_str += (n + '\n')
            mean_str += '\n'
        result = '%s\n%s' % (ph_str, mean_str)
        return result
    else:
        return 'None'


if __name__ == '__main__':
    print(translate('hello'))