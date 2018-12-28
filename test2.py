'''
test2.py : 자료형
 변수 선언이 가능하지만 필요 없다. 하지만 변수를 미리 선언하는 것이 더 효율적임.
'''
a = 100
b = 50
print(a,b)
print(a+b)
a,b = 100,50
print(a,b)
print(type(a))

#콘솔에서 입력받아 a 변수에 저장하기
a = int(input("첫번째숫자 : "))
b = int(input("두번째숫자 : "))
result = a + b
print(a,"+",b,"=",result)
result = a - b
print(a,"-",b,"=",result)
result = a * b
print(a,"*",b,"=",result)
result = a / b
print(a,"/",b,"=",result)
result = a % b
print(a,"%",b,"=",result)

# ** : 제곱, // : 나누기 이후에 소숫점 제거
print("9의 제곱 : ",9**2,", 나누기 정수값 : ",a//b)
print("a","b","c")
print("a"+"b"+"c")
print("abc" * 3)