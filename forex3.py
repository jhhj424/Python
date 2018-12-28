'''
Created on 2018. 12. 17.
forex3.py : 중첩반복문 구구단 출력하기
@author: a
'''

i,k = 0,0
for i in range(2,10,1) :
    for k in range(2,10,1) : 
        print("%d X %d = %3d" % (i,k,i*k))
    print("")