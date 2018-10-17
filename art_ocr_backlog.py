#!/usr/local/bin/python3.7
import pymysql

'''article ocr backlog'''

db = pymysql.connect(host='192.168.1.210',
                     user='root',
                     passwd='global01a',
                     db='noviny')

cur = db.cursor()
cur.execute('SELECT count(*) as ocr_article_backlog FROM `articles` \
WHERE `articles`.`is_relevant` = 0 \
AND `articles`.`is_captured` = 0 \
AND `is_ocr_done` = 0;')
res = cur.fetchall()
for row in res:
    print(row[0])

db.close()
