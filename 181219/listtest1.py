'''
Created on 2018. 12. 19.

@author: a
'''

# for문을 이용한 방법

aa = []
bb = []
for i in range(0,600) :
    if i % 3 == 0 :
        aa.append(i)
        bb.append(i)
bb.reverse()
print(bb[0])
print(bb[199])

# while 을 이용한 방법

aaa = []
bbb = []
num = 0
while True :
    if len(aaa) == 200 :
        break
    if num % 3 == 0 :
        aaa.append(num)
    num += 1

for i in range(0,200) :
    bbb.append(aaa[(len(aaa)-1)-i])
print(bbb[0])
print(bbb[199])