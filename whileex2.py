'''
Created on 2018. 12. 17.
whileex2.py
@author: a
'''

a,b,hap = 0,0,0

while True :
    a = int(input("첫번째 수를 입력하세요"))
    if a==0 :
        break
    b = int(input("두번째 수를 입력하세요"))
    hap = a + b
    print("%d + %d = %d" % (a,b,hap))
print("프로그램 종료")