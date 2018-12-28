'''
Created on 2018. 12. 24.

@author: a

dbex3.py : usertable 조회하기
'''
import sqlite3
con,cur = None,None
con = sqlite3.connect("iddb")
cur = con.cursor()
row = None

con = sqlite3.connect("iddb")
cur = con.cursor()

cur.execute("select * from usertable")
while True:
    row = cur.fetchone()#레코드 한개씩 조회
    if row == None: #데이터가 없는경우
        break
    print("%5s %15s %15s %d" % (row[0],row[1],row[2],row[3]))
con.close()