#!/usr/local/bin/python3.7
import pymysql


db = pymysql.connect(host='192.168.1.97',
                     user='grafana',
                     passwd='global01a',
                     db='videni')

cur = db.cursor()
cur.execute('select count(*) \
             from feeds f \
             left outer join feed_stt s on f.id=s.feed_id \
             where s.id is null')
res = cur.fetchall()
for row in res:
    print(row[0])

db.close()
