'''
Created on 2018. 12. 21.

@author: a

classEx6.py : 추상메서드 예제
'''
class SuperClass:
    def method(self):
        raise NotImplementedError # 하위 클래스에서 반드시 오버라이딩 필요
    
class SubClass1(SuperClass):
    def method(self):
        print("SubClass1 에서 method()를 오버라이딩함")
        
class SubClass2(SuperClass):
    #pass
    def method(self):
        print("SubClass2 에서 method()를 오버라이딩함")

sub1 = SubClass1()
sub2 = SubClass2()

sub1.method()
sub2.method()