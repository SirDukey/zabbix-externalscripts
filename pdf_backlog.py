#!/usr/local/bin/python3.7
import pymysql

db = pymysql.connect(host='192.168.1.210',
                     user='grafana',
                     passwd='global01a')

cur = db.cursor()
cur.execute("SELECT count(*) AS pdf_backlog FROM `noviny`.`articles`\
             WHERE `articles`.`filename` IS NULL AND `articles`.`content` !=''")
res = cur.fetchall()
for row in res:
    print(row[0])

db.close()
