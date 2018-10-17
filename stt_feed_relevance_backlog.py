#!/usr/local/bin/python3.7

import pymysql

'''Check size of Galera cluster'''

db = pymysql.connect(host='192.168.1.97',
                     user='grafana',
                     passwd='global01a',
                     db='videni')

cur = db.cursor()
cur.execute("select count(*) from feed_relevance fr \
             where fr.is_feed_rejected = 0 \
             and fr.is_feed_locked = 0 \
             and fr.is_captured = 0;")
res = cur.fetchall()
for row in res:
    print(row[0])

db.close()

