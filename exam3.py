'''
Created on 2018. 12. 17.
exam3 : 컴퓨터가 1부터 100사이의 임의의 정수를 저장하고
            새로운 수를 입력받아 저장된 수를 맞추기.
            저장된 수가 입력된 수보다 작으면 작은수 입니다.
            크면 큰수입니다.
            일치하면 정답입니다. 를 출력하기
            최종 정답까지 입력된 값의 갯수를 출력하기
            
@author: a
'''
import random

cnt,i = 0,0
ran = random.randrange(1,100)
print("1~100 사이에서 숫자를 맞춰보랑깨~")
while ran != i :
    i = int(input("숫자를 입력하세요 : "))
    cnt = cnt + 1
    if ran > i :
        print("큰수입니다.")
    elif ran < i :
        print("작은수입니다.")
    else : break
print("정답입니다!! %d번 만에 맞추셨습니다." % cnt)