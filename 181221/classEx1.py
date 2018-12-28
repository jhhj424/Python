'''
Created on 2018. 12. 21.

@author: a

classEx1.py : 클래스 예제
'''
#기본생성자 제공: __init__(self):
#               pass
class Car :
    color = '' #필드
    speed = 0 #필드
    
    def upSpeed(self,value): # self = java에서의 this ##메서드
        self.speed += value
    def downSpeed(self,value): ##메서드
        self.speed -= value

myCar1 = Car() # 객체화.
myCar1.color = "빨강"
myCar1.speed = 0
myCar2 = Car()
myCar2.color = "파랑"
myCar2.speed = 0
myCar3 = Car()
myCar3.color = "노랑"
myCar3.speed = 0

myCar1.upSpeed(30)
print("자동차1의 색상은 %s 이며, 현재 속도는 %dkm 입니다." % (myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print("자동차2의 색상은 %s 이며, 현재 속도는 %dkm 입니다." % (myCar2.color, myCar2.speed))

myCar3.upSpeed(10)
print("자동차3의 색상은 %s 이며, 현재 속도는 %dkm 입니다." % (myCar3.color, myCar3.speed))