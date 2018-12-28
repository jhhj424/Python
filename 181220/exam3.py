'''
Created on 2018. 12. 20.

@author: a
exam3.py
1.숫자1, 연산자, 숫자2 순서로 입력받는다.
2.제곱(**)연산자를 추가한다.
3.0으로 나누려고 하면 메세지를 출력하고 계산되지 않도록 한다.
'''
num1 = int(input("첫 번째 수를 입력하세요:"))
op = str(input("계산을 입력하세요(+,-,*,/,**):"))
num2 = int(input("두 번째 수를 입력하세요:"))


def calc(num1, num2, op):
    result = 0
    if op == "+" :
        result = num1 + num2
        print(num1, op, num2, "=", result)
    elif op == "-" :
        result = num1 - num2
        print(num1, op, num2, "=", result)
    elif op == "*" :
        result = num1 * num2
        print(num1, op, num2, "=", result)
    elif op == "/" :
        result = num1 / num2
        print(num1, op, num2, "=", result)
    elif op == "**" :
        result = num1 ** num2
        print(num1, op, num2, "=", result)
    else :
        print("연산자를 잘못 입력하셨습니다.")

        
try :
    calc(num1, num2, op)
except ZeroDivisionError :
        print("0으로 나눌 수 없습니다.")
