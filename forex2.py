'''
Created on 2018. 12. 17.
forex2.py : for 구문 연습
@author: a
'''

i,hap = 0,0
n1,n2,n3 = 0,0,0
n1 = int(input("시작값 입력: "))
n2 = int(input("끝값 입력: "))
n3 = int(input("증가값 입력: "))

for i in range(n1,n2+1,n3) :
    hap = hap + i
    
print("%d에서 %d까지 %d씩 증가시킨값의 합 :%d" % (n1,n2,n3,hap))