'''
Created on 2018. 12. 18.
exam9.py : c:/temp/data1.txt 파일을 읽어 화면에 출력하기

infp.readline() : 한줄씩 읽기
infp.readlines() : 한꺼번에 읽기
@author: a
'''

infp = None
inStr = ""

infp = open("c:/temp/data1.txt","rt")
while True :
    inStr = infp.readline()
    if not inStr :
        break
    print(inStr, end="")
infp.close()

print("===================")

infp = open("c:/temp/data1_UTF8.txt","rt",encoding="utf-8")
inStr = infp.readlines()
for s in inStr :
    print(s,end="")
infp.close()