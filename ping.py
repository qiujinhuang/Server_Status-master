#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import requests
from datetime import datetime

if __name__ == '__main__':
    timeout = 10
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    key = 'SCU23125Tb6ce03ba1324d2d6d55c98d31ffe17275aa8e513b22c5'
    title = "VPS在线检测"
    hostname = "127.0.0.1"
    response = os.system("ping "+ hostname)
    if response != 0:
        content = "VPS已无法连接" + "\n" + time
        payload = {
            'text': title,
            'desp': content
        }
        url = 'https://sc.ftqq.com/{}.send'.format(key)
        requests.post(url, params=payload, timeout=timeout)
    else:
        content = "VPS正常连接" + "\n" + time
