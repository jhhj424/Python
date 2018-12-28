'''
Created on 2018. 12. 20.

@author: a
funcex2.py : 가변 매개변수 에제
'''
def para_func(* para): # 0개 이상 여러개의 매개변수 가능
    # para 변수의 자료형은 Tuple임. : 
    result = 0
    for num in para :
        result = result + num
    return result

hap = 0

hap = para_func(10,20)
print("para_func(10,20) = %d" % hap)
hap = para_func(10,20,30)
print("para_func(10,20,30) = %d" % hap)
hap = para_func(10,20,30,40,50,60,70,80,90)
print("para_func(10,20,30,40,50,60,70,80,90) = %d" % hap)