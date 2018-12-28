'''
Created on 2018. 12. 17.

다음은 알파벳과 숫자를 아래에 주어진 암호표로 암호화하는 프로그램을 작성하시오

a b c d e f g h i j k l m n o p q r s t u v w x y z 
` ~ ! @ # $ % ^ & * ( ) - _ + = | [ ] { } ; : , . /

0 1 2 3 4 5 6 7 8 9 
q w e r t y u i o p

1. 암호화하기
src:abc123 
result:`~!wer


2. 복호화하기
src:`~!wer
result:abc123 

@author: a
'''
cen = "a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9"
pen = "` ~ ! @ # $ % ^ & * ( ) - _ + = | [ ] { } ; : , . / q w e r t y u i o p"
src = input("암호화 할 문자를 입력하세요! \n")
result = ""
for i in range(0,src.__len__()) :
    for j in range(0,len(pen)) :
        if cen[j] == src[i] :
            result += pen[j]
print(result)


src = input("복호화 할 문자를 입력하세요! \n")
result = ""
for i in range(0,len(src)) :
    for j in range(0,pen.__len__()) :
        if pen[j] == src[i] :
            result += cen[j]
print(result)