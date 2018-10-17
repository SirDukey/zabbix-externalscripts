#!/opt/rh/rh-python36/root#!/usr/local/bin/python3.7
import pymysql

'''WSREP local send queue for Galera cluster'''

db = pymysql.connect(host='192.168.1.12',
                     user='grafana',
                     passwd='global01a')

cur = db.cursor()
cur.execute("SHOW STATUS LIKE 'wsrep_local_send_queue_avg';")
res = cur.fetchall()
for row in res:
    print(row[1])
db.close()
