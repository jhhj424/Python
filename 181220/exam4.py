'''
Created on 2018. 12. 20.

@author: a

exam18.py : 0과 1부터 시작하는 피보나치 수열 구하기

0,1,1,2,3,5,8,13,21...

입력값 : 5
    0,1,1,2,3
입력값: 10
    0,1,1,2,3,5,8,13,21,34
'''

count = int(input("몇개의 피보나치 수열을 구할지 입력하세요\n"))
num = 0
pi = []
for i in range(0, count) :
    if len(pi) > 1 :
        pi.append(pi[num] + pi[num + 1])
        num += 1
    elif len(pi) == 1:
        pi.append(pi[num] + 1)
    else :
        pi.append(num)
print(pi)

print("\n두번째방법")
pi = [0,1]
for i in range(count) :
    if i > 1 :
        pi.append(pi[i-2]+pi[i-1])
print(pi)

print("\n세번째방법 : 재귀 함수")
num1 = 0
num2 = 1
temp = 0
pi=[]
def func(count):
    global num1,num2,temp
    if count > 0:
        pi.append(num1)
        temp = num1        
        num1 = num2
        num2 = temp + num1     
        func(count-1)
    else :
        return
func(count)
print(pi)

print("\n네번째방법 : 재귀 함수")
fibolist = []
def fibo(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
for i in range(0,count) :
    fibolist.append(fibo(i))
print(fibolist)