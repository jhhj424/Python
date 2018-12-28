'''
Created on 2018. 12. 18.
exam8.py : 문자를 '(내용)' 형태로 입력받기로 함. ( ) 입력을 안하면 ( )추가하기

startswith, endswith 함수 이용하기
@author: a
'''

ss = input("문자열을 입력하세요:")
print("출력 문자열:" , end="")
result = ""
if ss.startswith("(") == False :
    result += "("
for i in range(0,len(ss)) :
    result += ss[i]
if ss.endswith(")") ==False :
    result += ")"
print(result)
