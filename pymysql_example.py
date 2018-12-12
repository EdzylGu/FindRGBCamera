#!/usr/bin/env python
import os
import time
import sys
import pymysql


conn = pymysql.connect(host='127.0.0.1',user='root',passwd="1234",db='bit' ) 
cur = conn.cursor() 
#cur.execute ("mysqldump -u'root' -p'1234' red > red.sql")

cur.execute ("SELECT * FROM user") 
for r in cur : 
    print (r) 
cur.close () 
conn.close()

