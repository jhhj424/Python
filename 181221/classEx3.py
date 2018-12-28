'''
Created on 2018. 12. 21.

@author: a

classEx3.py : 인스턴스 변수, 클래스 변수
    인스턴스변수, 클래스변수는 선언부분에 차이가 없다.
    인스턴스변수 : self.변수명
    클래스변수  : 클래스명. 변수명 사용함.
'''

class Car :
    color = "" #인스턴스변수
    speed = 0
    count = 0
    
    def __init__(self,v1="빨강",v2=0): ## 기본생성자
        self.speed = v2
        self.color = v1
        Car.count +=1 #클래스 변수
    
    def printMessage(self):
        print("테스트 메세지 입니다.")
    def upSpeed(self,value): # self = java에서의 this
        self.speed += value
    def downSpeed(self,value):
        self.speed -= value
myCar1,myCar2 = None,None

myCar1 = Car()
myCar1.speed=30
print("자동차1의 색상은 %s 이며, 현재 속도는 %dkm 이며, 생상된 자동차는 총 %d대 입니다." % (myCar1.color, myCar1.speed,myCar1.count))
myCar2 = Car("파랑",20)
myCar2.speed=60
print("자동차1의 색상은 %s 이며, 현재 속도는 %dkm 이며, 생상된 자동차는 총 %d대 입니다." % (myCar2.color, myCar2.speed,myCar2.count))