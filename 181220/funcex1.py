'''
Created on 2018. 12. 20.

@author: a
funcex1.py : 반환값이 여러개인 경우 처리
'''
def multi(v1,v2):
    retList = []
    res1 = v1 + v2
    res2 = v1 - v2
    retList.append(res1)
    retList.append(res2)
    return retList

myList = []
hap,sub = 0,0

myList = multi(100, 200)
hap = myList[0]
sub = myList[1]
print("multi 함수의 리턴값 : %d, %d" % (hap,sub))