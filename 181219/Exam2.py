'''
Created on 2018. 12. 19.

@author: a
'''
parking = []


def push(car):
    parking.append(car)


def pop():
    return parking.pop()

'''
ord(car) : 'A' 의 아스키코드값
chr(ord(car) + i) : 아스키값을 문자열로 변경
'''

if __name__ == '__main__' :
    car = 'A';
    for i in range(0, 3) :
        push("자동차" + chr(ord(car) + i))
        print(parking)
        
    for i in range(0, 3) :
        print(pop(), end=",")