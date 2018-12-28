'''
Created on 2018. 12. 21.

@author: a
multiprocessex1.py : 멀티프로세싱구현하기
'''
import time
import multiprocessing
class RacingCar:
    carName = ""
    def __init__(self,name):
        self.carName = name
        
    def runCar(self):
        for _ in range(0,3):
            carStr = self.carName + "~~ 달립니다.\n"
            print(carStr,end="")
            time.sleep(0.1)
            
if __name__ == '__main__':
    car1 = RacingCar("@자동차1")
    car2 = RacingCar("#자동차2")
    car3 = RacingCar("$자동차3")
    mp1 = multiprocessing.Process(target=car1.runCar)
    mp2 = multiprocessing.Process(target=car2.runCar)
    mp3 = multiprocessing.Process(target=car3.runCar)
    mp1.start() #프로세스 실행 시작
    mp2.start()
    mp3.start()
    mp1.join() #mp1 프로세스가 졸요할때 까지 main이 대기 java의 waitfor 랑 똑같음
    mp2.join()
    mp3.join()
    print("프로그램종료")
