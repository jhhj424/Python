'''
Created on 2018. 12. 20.

@author: a

exam1.py : 문자열 변경하여 출력하기
'''
ss = "파이썬은완전재미있어요"
#파#썬#완#재#있#요 출력하기
for i in range(0,len(ss),2) :
    print("#%s" % ss[i], end="")
print()

# 모든 공백을 제거하기
ss = " 파 이 썬  "
print(ss.replace(" ", ""))

# 특정 문자 제거하기
print("\n특정 문자 제거하기")
ss1 = "-----파--이--썬-----"
ss2 = "<<<<<파<<이>>썬>>>>>"
print(ss1.strip("-"))
print(ss2.strip("<>"))