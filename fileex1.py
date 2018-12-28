'''
Created on 2018. 12. 18.
fileex1.py : 파일 읽기
@author: a
'''

infp = None
inStr = ""
'''
    open(파일이름, 파일 열기 모드)
    
파일 열기 모드
    "r" : 읽기모드, 기본값
    "w" 쓰기모드, 존재하면 덮어쓴다.
    "r+" : 읽기/ 쓰기 겸용
    "a" : 쓰기모드 , append모드, 존재하는 파일인 경우 이어서 쓴다.
    "t" : 텍스트모드, 파일의 종류, 기본값
    "b" : 이진모드, 
'''

infp = open("c:/temp/data1.txt","rt")
inStr = infp.readline()
print(inStr,end="%")
inStr = infp.readline()
print(inStr,end="*")
inStr = infp.readline()
print(inStr,end="!")
infp.close()