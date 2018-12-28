'''
Created on 2018. 12. 19.

@author: a
'''
cars = []

def Top(list,int) : 
    if int == 1 :
        print("자동차가 다음에 들어갈 위치는{}입니다.".format(len(list)))
    return len(list)

def Push(list,str):
    print("{}가 주차되었습니다.".format(str))
    list.append(str)
    
def Pop(list,int):
    print("{}가 나갔습니다.".format(cars[int]))
    list.pop(int)

while True :
    action = input("숫자를 입력하세요. 1:주차, 2:차빼기, 3:주차된 차목록, 4:프로그램종료\n")
    if action == "1" :
        str = input("주차시킬 자동차를 입력하세요\n")
        Push(cars, str)
    elif action == "2" :
        if len(cars) == 0 :
            print("주차된 차가 없습니다. 다시 입력해주세요\n")
            continue
        if len(cars) > 0 :
            Pop(cars,len(cars)-1)
    elif action == "3" :
        if len(cars) == 0 :
            print("주차된 차가 없습니다.\n")
        else :
            print(cars)
    elif action == "4" :
        print("프로그램종료")
        print("주차된 자동차 :" , cars)
        break
    else :
        print("숫자를 잘못입력하셨습니다. 다시 입력해주세요\n")