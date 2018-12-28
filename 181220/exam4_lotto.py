'''
Created on 2018. 12. 20.

@author: a
'''
import random
from matplotlib.pyplot import plotting


# #함수 선언 부분
def getNumber() :
    return random.randrange(1, 46)


# 전역 변수 선언 부분##
lotto = []
num = 0
# # 메인 코드 부분
print("**로또 추첨을 시작합니다.**\n");

while True :
    num = getNumber()
    if len(lotto) > 6 :
        break
    if lotto.count(num) == 0 :
        lotto.append(num)

print("추첨된 로또 번호 ==> ", end="")
lotto.sort()
for i in lotto :
    print(i, end=" ")
