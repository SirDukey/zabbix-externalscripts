#!/opt/rh/rh-python36/root#!/usr/local/bin/python3.7

from haproxystats import HAProxyServer

haproxy = HAProxyServer('192.168.1.13:9600')
'''
output = []
for b in haproxy.backends:
    output.append(b.status)
if 'UP' in output[1]:
    print(10)
else:
    print(0)
'''
print(haproxy.to_json())
