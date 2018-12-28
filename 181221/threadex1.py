'''
Created on 2018. 12. 21.

@author: a
threadex1.py : 스레드 구현하기
'''
import time
import threading
class RacingCar:
    carName = ""
    def __init__(self,name):
        self.carName = name
        
    def runCar(self):
        for _ in range(0,3):
            carStr = self.carName + "~~ 달립니다.\n"
            print(carStr,end="")
            time.sleep(0.1)
car1 = RacingCar("@자동차1")
car2 = RacingCar("#자동차2")
car3 = RacingCar("$자동차3")
#스레드 객체 생성
# target-car1.runCar : 스레드가 실행해야할 메서드 지정
th1 = threading.Thread(target=car1.runCar)
th2 = threading.Thread(target=car2.runCar)
th3 = threading.Thread(target=car3.runCar)
th1.start() #스레드 시작 : 병렬화처리, runCar메서드 호출
th2.start()
th3.start()
print("프로그램종료")
