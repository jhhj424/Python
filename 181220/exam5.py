'''
Created on 2018. 12. 20.

@author: a
exam5.py : 파일을 읽어서 라인수와 내용을 화면에 출력하기
'''
infp = None
inStr = ""
infp = open("c:/temp/data1.txt","r")
line = 0
while True :
    inStr = infp.readline()
    line += 1
    if inStr == "" :
        break
    print("%d:%s" % (line,inStr), end="")
infp.close()