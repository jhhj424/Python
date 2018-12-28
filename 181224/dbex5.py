'''
Created on 2018. 12. 24.

@author: a
dbex5.py : mariadb와 연동하기 
'''
import pymysql # pip3 install pymysql 설정 필요

conn = pymysql.connect(host="localhost",port=3306,user="scott",passwd="tiger",db="bigdb",charset="utf8")
try:
    cur = conn.cursor()
    cur.execute("select * from item")
#    while True :
#        row = cur.fetchone()
#        if row == None:
#            break
#        print(row)
    for row in cur.fetchall() :
        print(row)
finally:
    cur.close()
    conn.close()