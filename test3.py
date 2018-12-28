'''
Created on 2018. 12. 17.

test3.py : 문자열 출력하기

@author: a
'''
print("안녕하세요")
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[-1])
print("안녕하세요"[-2])
print("안녕하세요"[1:3]) #인덱스1부터 3인덱스 앞까지
print("안녕하세요"[:3]) #인덱스0부터 3인덱스 앞까지 // 앞에서부터 3개
print("안녕하세요"[3:]) #3번 인덱스 이후 모두

print("자료형 조회하기 : type")
s = "반갑습니다."
print(type(s))
print(len(s))
print(type(len(s)))

arr = [10,20,30,40,50,60,70]
print(arr[:2]) # [10, 20]
print(arr[::2]) # [10, 30, 50, 70]
print(arr[::-2])
print(arr[::-1])