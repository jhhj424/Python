'''
Created on 2018. 12. 17.
exam4 : 문제 : 삼각형 찍기
@author: a
'''
type = int(input("삼각형의 종류를 입력하세요 ! 1~3 : "))
hight = int(input("삼각형의 높이를 입력하세요! : "))
if type == 1 :
    for i in range(1,hight+1) :
        star = "*"
        print(star * i)
elif type == 2 :
    for i in range(hight,0,-1) :
        star = "*"
        print(star * i)
elif type == 3 : # 일반 문자열을 이용한 이등변 삼각형
    for i in range(1,hight+1) :
        num = (hight-i) 
        star = " " * num
        s = "*" * (i * 2 -1)
        print(star + s)
else :
    print("삼각형의 종류를 잘못 입력하셨습니다.")