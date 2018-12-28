'''
Created on 2018. 12. 20.

@author: a
yield.py : 제너레이터와, yield 예약어
        yield : 함수의 종료 없이 값을 리스트로 반환함
'''
def genFun(num):
    for i in range(10,num+10) :
        yield i
        print(i,"값 반환")
    
print(list(genFun(5)))

for data in genFun(5) :
    print("main에서 출력:" , data)