'''
Created on 2018. 12. 20.

@author: a
varex1.py : 변수 설명
'''

def func1() :
    global a; #a 변수는 전역변수를 사용함
    a = 10
    print("func1()에서 a 값 %d" % a) #전역변수 a
    
def func2() :
    print("func2()에서 a 값 %d" % a) #전역변수 a
    
a = 20

func1() #10
func2() #10