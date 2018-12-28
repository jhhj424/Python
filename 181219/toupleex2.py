'''
Created on 2018. 12. 19.

@author: a
toupleex2.py : 튜플 -> 리스트 -> 튜플 변환하기
'''

myTuple =(10,20,30)
myList = list(myTuple)
myList.append(40)
myTuple = tuple(myList)
print(myTuple)