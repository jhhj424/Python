'''
Created on 2018. 12. 17.
forex1.py : 반복문 for 연습
@author: a
'''
import random ## 기능을 사용하기 위한 객체를 include
import keyword


numbers = [] # 배열선언, 리스트라고도 함
for num in range(0,10) : #num 의 값이 0부터 9까지 1씩 증가하면서 반복함
    numbers.append(random.randrange(0,10)) #0부터 9까지의 임의의 값
print("생성된 리스트",numbers)

for num in range(0,10) :
    if num not in numbers :
        print("숫자 %d는 리스트에 없습니다." % num)
        
print(keyword.kwlist) #파이썬에서 사용되는 예약어 목록 출력함.