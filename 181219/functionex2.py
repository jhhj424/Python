'''
Created on 2018. 12. 19.

@author: a

functionex2.py : 함수 정의
'''

def getMean(numbericValue) :#numbericValue : 숫자형태 값
    # \ : 다음줄표현 - 다음줄도 연결해서 한줄로 
    return sum(numbericValue)/len(numbericValue)\
        if len(numbericValue) > 0\
        else float("NaN")#매개변수의 숫자목록 길이가 0보다 크지 않으면 NaN
        
my_list = [2,2,2,4,4,6,6,8,8]
print("output #1(mean): {!s}".format(getMean(my_list)))

my_empty = []
print("output #1(mean): {!s}".format(getMean(my_empty)))