'''
Created on 2018. 12. 20.

@author: a
Lambdaex1.py : 람다표현식
'''
def hap(num1,num2):
    res = num1 + num2
    return res

print(hap(10,20))

hap2 = lambda num1,num2:num1+num2
print(hap2(10,20))

hap3 = lambda num1=10,num2=20:num1+num2
print(hap3())
print(hap3(100))
print(hap3(100,200))