#!/usr/local/bin/python3.7

import subprocess as sp

cmd = ['veeamconfig session list --24']
res = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
output, error = res.communicate()
output = output.decode('ascii')
error = error.decode('ascii')

my_list = []
my_list.append(output.split(' '))

val = my_list[0][-9]
if 'Success' in val:
    print(10)
elif 'Running' in val:
    print(20)
elif 'Failed' in val:
    print(40)
else:
    print(30)
