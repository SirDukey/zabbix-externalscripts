#!/usr/local/bin/python3.7
import pymysql

'''pdf generating backlog'''

db = pymysql.connect(host='192.168.1.210',
                     user='root',
                     passwd='global01a',
                     db='noviny')

cur = db.cursor()
cur.execute('SELECT count(*) as pdf_backlog FROM `articles` \
             WHERE `articles`.`filename` is null \
             AND `articles`.`content` != ""')
res = cur.fetchall()
for row in res:
    print(row[0])

db.close()
