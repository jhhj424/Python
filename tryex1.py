'''
Created on 2018. 12. 18.

@author: a

tryex1.py : 예외 처리 예제
'''

myStr = "파이썬 공부 중입니다. 파이썬은 쉽습니다."
strPosList = []
index = 0
while True :
    try :
        index = myStr.index("파이썬", index) # 파이썬 문자의 위치를 index 값 이후에서 검색
        strPosList.append(index) # 0 13
        index += 1
    except :
        break
print("파이썬 문자의 위치:" , strPosList)