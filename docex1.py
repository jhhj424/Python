'''
Created on 2018. 12. 18.
dicex1.py : 딕셔너리 예제
@author: a
'''

singer = {}
singer['이름'] = '트와이스'
singer['구성원수'] = 9
singer['데뷰'] = "서바이벌 식스틴"
singer['대표곡'] = 'signal'

for i in singer.keys() :
    print("%s = %s" % (i,singer[i]))
    
print(type(singer))
print(type(singer.keys()))
print(type(list(singer.keys())))