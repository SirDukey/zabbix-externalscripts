#!/usr/local/bin/python3.7

import urllib3
import json

http = urllib3.PoolManager()
url = 'http://httpbin.org/ip'
resp = http.request('GET', url)
data = json.loads(resp.data.decode('utf-8'))
ip = list(data.values())[0]

if '154.65.43.80' in ip:
    print(1)
elif '105.27.154.46' in ip:
    print(2)
else:
    print(0)
