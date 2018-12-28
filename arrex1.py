'''
Created on 2018. 12. 18.
arrex1.py : 배열 예제 => 리스트 라 함.
@author: a
'''

aa = [0,0,0,0]
hap = 0

for i in range(0,4) :
    aa[i] = int(input(str(i+1) + " 번째 숫자 :"))
    hap += aa[i]
print("합계:",hap)