'''
Created on 2018. 12. 21.

@author: a
classEx4.py : 상속 예제
'''

class Car :
    speed = 0
    def upSpeed(self,value):
        self.speed += value
        print("현재속도(부모클래스) : %d" % self.speed)
        
class Sedan(Car):
    def upSpeed(self, value):
        self.speed +=value
        if self.speed > 150 :
            self.speed = 150
            print("현재속도(자손클래스) : %d" % self.speed)
            
class Truck(Car):
    pass

sedan1,truck1 = None,None

truck1 = Truck()
sedan1 = Sedan()
print("트럭->",end="")
truck1.upSpeed(200)
print("승용차->",end="")
sedan1.upSpeed(200)