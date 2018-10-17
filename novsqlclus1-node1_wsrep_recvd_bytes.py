#!/opt/rh/rh-python36/root#!/usr/local/bin/python3.7
import pymysql

'''WSREP local recieve queue for Galera cluster'''

db = pymysql.connect(host='192.168.1.11',
                     user='grafana',
                     passwd='global01a')

cur = db.cursor()
cur.execute("SHOW STATUS LIKE 'wsrep_received_bytes';")
res = cur.fetchall()
for row in res:
    print(row[1])
db.close()
