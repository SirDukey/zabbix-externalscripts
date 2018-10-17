#!/usr/local/bin/python3.7
import pymysql

'''page ocr backlog'''

db = pymysql.connect(host='192.168.1.210',
                     user='root',
                     passwd='global01a',
                     db='noviny')

cur = db.cursor()
cur.execute('SELECT count(*) - 124 as ocr_pages_backlog FROM `pages` \
             WHERE `pages`.`is_relevant`= 0 \
             AND `pages`.`is_fully_processed`= 0 \
             AND `pages`.`is_ocr_done`= 0;')
res = cur.fetchall()
for row in res:
    print(row[0])

db.close()
