'''
Created on 2018. 12. 18.
exam8.py : 문자를 '(내용)' 형태로 입력받기로 함. ( ) 입력을 안하면 ( )추가하기

startswith, endswith 함수 이용하기
@author: a
'''

while True :
    s = str(input("문자입력하셈"))
    if s.startswith("(") & s.endswith(")") :
        print(s)
    elif s.startswith("(") :
        print("%s)" % s)
    elif s.endswith(")") :
        print("(%s" % s)
    elif s == "끝" :
        break
    else :
        print("(%s)" % s)
