'''
Created on 2018. 12. 17.
forex4.py : 가로 구구단 출력하기
@author: a
'''
i,k = 0,0
for i in range(2,10,1) :
    print("  %d단                " % i,end=" ")
print()
for i in range(2,10,1) :
    for k in range(2,10,1) :
        print("%d X %d =%3d " % (k,i,k*i),end=" ")
    print("")
    
    
    
i,j,line = 0,0,""
for i in range(2,10) :
    line = line + ("   %d단                " % i)
print(line)

for i in range(2,10) : 
    line = ""
    for k in range (2,10) :
        line = line + ("%2d X%2d = %2d " % (k,i,k*i))
    print(line)