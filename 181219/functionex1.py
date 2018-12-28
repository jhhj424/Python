'''
Created on 2018. 12. 19.

@author: a

functionex1.py : 함수 사용하기
'''

def myFunc() :
    print("myFunc() 함수 호출함")

def main() :
    print("메인 함수 부분입니다. 여기부터 실행 됩니다.")
    myFunc()
    print("전역변수 gvar 값:",gvar)

gvar = 100

if __name__=='__main__' : #프로그램의 시작점
    main()