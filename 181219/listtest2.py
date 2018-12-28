'''
Created on 2018. 12. 19.

@author: a

listtest2.py : 
tt = ((1,2,3),(4,5,6),(7,8,9))
의 모든 값을 출력하기
'''

tt = ((1, 2, 3)), ((4, 5, 6)), ((7, 8, 9))

print(tt) 
for i in range(0, len(tt)):
    for j in range(0, len(tt[i])):
        print(tt[i][j], end=" ")
    print()