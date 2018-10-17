#!/usr/local/bin/python3.7
import pymysql


db = pymysql.connect(host='192.168.1.97',
                     user='grafana',
                     passwd='global01a',
                     db='videni')

cur = db.cursor()
cur.execute('select count(*) from tmp_stt_files where is_sent = 0')
res = cur.fetchall()
for row in res:
    print(row[0])

db.close()
