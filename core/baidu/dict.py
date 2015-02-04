#!/usr/env/python3
# -*-coding:utf-8-*-

"""
documentary
"""
import json
from urllib import request, parse

__author__ = 'skitta'


class Client():
    def __init__(self, api_key):
        self.URL = 'http://openapi.baidu.com/public/2.0/translate/dict/simple?'
        self.API_KEY = api_key

    def api_request(self, tran_str, tran_from='auto', tran_to='auto'):
        body = {
            'client_id': self.API_KEY,
            'q': tran_str,
            'from': tran_from,
            'to': tran_to
        }
        url = self.URL + parse.urlencode(body)
        req = request.Request(url)
        return req

    @classmethod
    def api_response(cls, api_request):
        try:
            resp = request.urlopen(api_request)
        except IOError:
            return 'NetWork Error'
        except Exception as error:
            return str(error)
        else:
            data = json.loads(resp.read().decode())
            return data


def translate(word):
    client = Client('efVWN2paqPC7xrIPklvfVk0l')
    req = client.api_request(word)
    resp = client.api_response(req)
    if isinstance(resp, dict):
        if resp['data']:
            data = resp['data']['symbols'][0]
            return __data_handle(data)
        else:
            return word
    else:
        return resp


def __data_handle(data):
    ph_str = ''
    if 'ph_zh' in data:
        if data['ph_zh']:
            ph_str += 'Ping Yin:[' + data['ph_zh'] + ']\n'
    if 'ph_en' in data:
        if data['ph_en']:
            ph_str += 'EN:[' + data['ph_en'] + ']\n'
    if 'ph_am' in data:
        if data['ph_am']:
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
