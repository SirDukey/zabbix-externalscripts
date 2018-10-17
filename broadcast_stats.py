#!/usr/local/bin/python3.7
import PyMySQL 

db = PyMySQL.connect('192.168.1.210','root','global01a','print')
cursor = db.cursor()

query1 = 'SHOW TABLES;'
res = cursor.execute(query1)
for row in res:
    print(row)
db.close()
