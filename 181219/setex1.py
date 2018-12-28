'''
Created on 2018. 12. 19.

@author: a

setex1.py : set 예제
'''

mySet1 = {1,2,3,4,5}
mySet2 = {4,5,6,7}

numSet1 = {1,2,3,3,4,4,5,5,6} # set은 중복 X
print(numSet1) #{1, 2, 3, 4, 5, 6}

#교집합
print(mySet1 & mySet2)#{4, 5}
print(mySet1.intersection(mySet2))#{4, 5}

#합집합
print(mySet1 | mySet2)#{1, 2, 3, 4, 5, 6, 7}
print(mySet1.union(mySet2))#{1, 2, 3, 4, 5, 6, 7}

#차집합
print(mySet1 - mySet2)#{1, 2, 3}
print(mySet1.difference(mySet2))#{1, 2, 3}

#대칭차집합
print(mySet1 ^ mySet2)#{1, 2, 3, 6, 7}
print(mySet1.symmetric_difference(mySet2))#{1, 2, 3, 6, 7}