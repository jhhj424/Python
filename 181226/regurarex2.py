'''
Created on 2018. 12. 26.

@author: a
regurarex2.py : 정규식을 이용하여 regurarex1.py와 같은 결과 얻기
'''
import re #정규식을 사용하기 위한 모듈
data = '''
    park 800905-1234567
    kin  700905-1234567
    choi 850101-a123456
'''

'''
    () : 그룹지정
    [] : 문자지정
    {} : 갯수
    \d : 숫자
    (\d{6})[-]\d{7} : 패턴지정
    \g<1> : 첫번째 그룹
    
    ? : 0또는 1개인 경우
        ca?t : a문자가 없거나  1개인 경우
                "ct" : true
                "cat" : true
                "caaaaaaaaaaaaaaaat" : false
    * : 0개이상 반복의미
        ca*t : a문자가 0개 이상인 경우. : 없어도됨.
                "ct" : true
                "cat" : true
                "caaaaaaaaaaaaaaaat" : true
    + : 1개이상 반복의미
        ca+t : a문자가 1개 이상인 경우. : 반드시 한개 이상 있어야함
                "ct" : false
                "cat" : true
                "caaaaaaaaaaaaaaaat" : true
 {n} : n개 반복
      ca{2}t : a문자가 2개 반복
                "ct" : false
                "cat" : false
                "caat" : true
                "caaaaaaaaaaaaaaaat" : false
 {n,m} : n에서 m개까지 반복
       ca{2,5}t : a문자가 2개에서 5개까지 반복
                "ct" : false
                "cat" : false
                "caat" : true
                "caaaaat" : true
                "caaaaaaaaaaaaaaaat" : false
'''
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******",data))