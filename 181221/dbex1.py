'''
Created on 2018. 12. 21.

@author: a
dbex1.py : sqlite3 db와 연결하기
'''
import sqlite3
dbpath = "test.sqlite" # db 저장파일이름
conn = sqlite3.connect(dbpath)
cur = conn.cursor() # 명령 전달 객체 생성
# 여러개의 sql구문을 실행 명령어
cur.executescript('''
    drop table if exists items;
    create table items (item_id integer primary key,
        name text unique,
        price integer);
    insert into items (name, price) values ('Apple',800);
    insert into items (name, price) values ('Orange',500);
    insert into items (name, price) values ('Banana',300);
''')
#트랜잭션 종료. 실제로 insert 구문이 실행됨
conn.commit()
cur = conn.cursor()
cur.execute("select item_id, name,price from items")
#cur.fetchall() : cur에 저장된 db read 정보를 조회
item_list = cur.fetchall()
for it in item_list :
    print(it)