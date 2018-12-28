'''
Created on 2018. 12. 24.

@author: a
dbex4.py : GUI 환경으로 만들기
'''
import sqlite3
from tkinter import *
from tkinter import messagebox

def insertData() :
    con,cur = None,None
    data1,data2,data3,data4 = "","","",""
    sql = ""
    con = sqlite3.connect("iddb")#db와 연결 객체
    cur = con.cursor()
    data1 = edit1.get() #입력된 값을 리턴
    data2 = edit2.get()
    data3 = edit3.get()
    data4 = edit4.get()
    try :
        sql = "insert into usertable values('" + data1+"','"+data2+"','" + data3 + "','" + data4+"')"
        cur.execute(sql)#db에등록
    except:
        messagebox.showerror("오류", "데이터 입력시 오류 발생")
    else: #입력성공
        messagebox.showinfo("성공", "데이터 입력 성공")
    finally:
        con.commit()
        con.close()
        
def selectData():
    strData1,strData2,strData3,strData4 = [],[],[],[]
    con = sqlite3.connect("iddb")
    cur = con.cursor()
    cur.execute("select * from usertable")
    strData1.append("사용자ID")
    strData2.append("사용자이름")
    strData3.append("이메일")
    strData4.append("출생연도")
    strData1.append("----------")
    strData2.append("----------")
    strData3.append("----------")
    strData4.append("----------")
    while True :
        row = cur.fetchone()
        if row == None :
            break
        strData1.append(row[0])
        strData2.append(row[1])
        strData3.append(row[2])
        strData4.append(row[3])
    listData1.delete(0,listData1.size() -1)
    listData2.delete(0,listData2.size() -1)
    listData3.delete(0,listData3.size() -1)
    listData4.delete(0,listData4.size() -1)
#zip(strData1,strData2,strData3,strData4) => 동일한 크기의 리스트를 연결하기
#    (strData1[0],strData2[0],strData3[0],strData4[0])
#    (strData1[1],strData2[1],strData3[1],strData4[1])
#db에서 읽은 내용을 추가
    for item1,item2,item3,item4 in zip(strData1,strData2,strData3,strData4):
        listData1.insert(END,item1)
        listData2.insert(END,item2)
        listData3.insert(END,item3)
        listData4.insert(END,item4)
    con.close()

window = Tk() ##GUI환경설정
window.geometry("600x300")
window.title("GUI 데이터 입력")

edtFrame = Frame(window)
edtFrame.pack()
listFrame = Frame(window)
listFrame.pack(side=BOTTOM,fill=BOTH,expand=1)

edit1 = Entry(edtFrame,width=10)# edit박스
edit1.pack(side=LEFT,padx=10,pady=10)
edit2 = Entry(edtFrame,width=10)
edit2.pack(side=LEFT,padx=10,pady=10)
edit3 = Entry(edtFrame,width=10)
edit3.pack(side=LEFT,padx=10,pady=10)
edit4 = Entry(edtFrame,width=10)
edit4.pack(side=LEFT,padx=10,pady=10)

#command = insertData : 클릭된 경우 insertData 함수 호출, 핸들러 설정
btnInsert = Button(edtFrame,text="입력",command=insertData)
btnInsert.pack(side=LEFT,padx=10,pady=10)
btnSelect = Button(edtFrame,text="조회",command=selectData)
btnSelect.pack(side=LEFT,padx=10,pady=10)

listData1 = Listbox(listFrame,bg="yellow")
listData1.pack(side=LEFT,fill=BOTH,expand=1)
listData2 = Listbox(listFrame,bg="yellow")
listData2.pack(side=LEFT,fill=BOTH,expand=1)
listData3 = Listbox(listFrame,bg="yellow")
listData3.pack(side=LEFT,fill=BOTH,expand=1)
listData4 = Listbox(listFrame,bg="yellow")
listData4.pack(side=LEFT,fill=BOTH,expand=1)
window.mainloop() ##GUI 화면 출력