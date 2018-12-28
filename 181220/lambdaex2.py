'''
Created on 2018. 12. 20.

@author: a
lambdaex2.py : 리스트에서 사용되는 람다식
'''

myList = [1,2,3,4,5]
def add10(num) :
    return num + 10

for i in range(len(myList)) :
    myList[i] = add10(myList[i])
print(myList)

add20 = lambda num:num+10
myList = list(map(add20,myList))
print(myList)

myList = list(map(lambda num:num+10, myList))
print(myList)

list1 = [1,2,3,4]
list2 = [10,20,30,40]

haplist = list(map(lambda n1,n2:n1+n2,list1,list2))
print(haplist)