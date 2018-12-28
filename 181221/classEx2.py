'''
Created on 2018. 12. 21.

@author: a

classEx2.py : 생성자 예제
    생성자는 __init__표현함.
    기본생성자 : 생성자의 매개변수가 self만 있는 생성자
'''

class Car :
    color = '' #인스턴스변수
    speed = 0
    
    def __init__(self,v1="빨강",v2=0): ## 생성자 #self : 매개변수 목록의 첫번째 매개변수여야함. 인자대입과 상관없음
        self.color = v1
        self.speed = v2
    
    def upSpeed(self,value): # self = java에서의 this
        self.speed += value
    def downSpeed(self,value):
        self.speed -= value
myCar1 = Car()
myCar2 = Car("파랑",20) #v1<=파랑  v2<=20 생성자의 값으로 매핑됨
print("자동차1의 색상은 %s 이며, 현재 속도는 %dkm 입니다." % (myCar1.color, myCar1.speed))
print("자동차1의 색상은 %s 이며, 현재 속도는 %dkm 입니다." % (myCar2.color, myCar2.speed))