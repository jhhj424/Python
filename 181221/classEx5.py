'''
Created on 2018. 12. 21.

@author: a
classEx5.py : 클래스에서 사용되는 지정된 특별한 메서드
'''
class Line :
    length = 0
    def __init__(self,length): ##생성자 : 객체 생성시 호풀되는 메서드
        self.length = length
        print(self.length,"길이의 선이 생성 되었습니다.")
    def __del__(self):        ##소멸자 : 객체 제거시 호출되는 메서드
        print(self.length,"길이의 선이 제거 되었습니다.")
    def __repr__(self):       ## 자바의 toString : 해당 객체의 출력을 담당하는 메서드
        return "선의 길이: "+str(self.length)
    def __add__(self,other):        #더하기 연산자 사용시 호풀되는 메서드
        return self.length + other.length
    def __lt__(self,other):         # < 연산자 사용시 호출되는 메서드
        return self.length < other.length
    def __eq__(self,other):
        return self.length == other.length
    
myLine1 = Line(100)     #객체화, 생성자 호출
myLine2 = Line(200)
print(myLine1)
print(myLine2)

print("두 선의 길이의 합:", myLine1 + myLine2)
if myLine1 < myLine2 :
    print("myLine2가 더 깁니다.")
elif myLine1 == myLine2 :
    print("두선분의 길이가 같습니다.")
else :
    print("myLine1가 더 깁니다.")
##프로그램 종료 : 생성된 객체가 자동으로 소멸됨. : 이때 객체의 소멸자 호출됨