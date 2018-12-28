'''
Created on 2018. 12. 24.

@author: a

dbex2.py : sqlite db 사용하기
'''
import sqlite3
con,cur = None,None
data1,data2,data3,data4 = "","","",""
con = sqlite3.connect("iddb")#db와 연결 객체
cur = con.cursor()           #db에 sql 구문 실행
#cur.executescript('''
#    create table usertable (id char(4) primary key,
#                 username char(15), email char(15), birthyear int)
#''')

while True :
    data1 = input("사용자 ID => ")
    if data1 == "" :
        break
    data2 = input("사용자 이름 =>")
    data3 = input("이메일 =>")
    data4 = input("출생년도 =>")
    sql = "insert into usertable values('" + data1+"','"+data2+"','" + data3 + "','" + data4+"')"
    cur.execute(sql)
    con.commit()
    con.close()