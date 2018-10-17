#!/opt/rh/rh-python36/root#!/usr/local/bin/python3.7
import pymysql

'''Check state of node of Galera cluster'''

db = pymysql.connect(host='192.168.1.11',
                     user='grafana',
                     passwd='global01a')

cur = db.cursor()
cur.execute("SHOW STATUS LIKE 'wsrep_local_state'")
res = cur.fetchall()
for row in res:
    print(row[1])

db.close()
