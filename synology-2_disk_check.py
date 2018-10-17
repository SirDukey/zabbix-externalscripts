#!/usr/local/bin/python3.7

import subprocess as sp

cmd = ["sshpass -p 'global01a' ssh admin@192.168.1.91 df -h | awk 'NR==9{print $3}' | tr -d 'T'"]
res = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
output, error = res.communicate()
output = output.decode('ascii')
error = error.decode('ascii')

print(output.strip('\n'))

