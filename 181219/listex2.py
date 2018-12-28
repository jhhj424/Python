'''
Created on 2018. 12. 19.

@author: a
listex2.py : 컴프리헨션
'''

#1부터 5까지 값을 저장
mylist = []
for i in range(1,6) :
    mylist.append(i)
print(mylist)

#컴프리헨션 형태로 구현하기
mylist = [num for num in range(1,6)]
print(mylist)

#1부터 100까지 숫자 중 3의 배수만 저장하는 리스트

mylist = []
for i in range(1,101) :
    if i%3 == 0 :
        mylist.append(i)
print(mylist)

mylist = [num for num in range(1,101) if num%3==0]
print(mylist)

mylist = [num for num in range(3,101,3)]
print(mylist)