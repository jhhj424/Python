'''
Created on 2018. 12. 18.
exam7 : 

ss 문자열을  홍#길#동#전# 출력하기

@author: a
'''

ss = "홍길동전"

print("문제1 : ss 문자열을  홍#길#동#전# 출력하기")

for i in range (0,len(ss)) :
    print("%s" % ss[i], end="#")
    
print("\n문제2 : ss 문자열을  거꾸로 출력하기")

for i in range (0,len(ss)) :
    print("%s" % ss[-i-1], end="")