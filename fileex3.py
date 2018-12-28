'''
Created on 2018. 12. 18.

@author: a

fileex3.py : utf-8 파일 읽기
'''

infp = None
inStr = ""
infp = open("c:/temp/data1_UTF8.txt","rt",encoding="utf-8")
while True :
    inStr = infp.readline()
    if inStr == "" :
        break
    print(inStr, end="")
infp.close()