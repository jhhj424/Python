'''
Created on 2018. 12. 18.
dicex3.py : dist 자료형과 list 자료형 연결
@author: a
'''
import operator

a = 10
print(type(a))
a = 1.5
print(type(a))

tranDic, tranList = {}, []
tranDic = {"Thomas":"토마스", "Edword":"에드워드","Henry":"헨리","Gothen":"고든","James":"제임스"}
#key = operator.itemgetter(0) : tranDic.items() 객체의 첫번째 데이터를 정렬의 기준 설정
tranList = sorted(tranDic.items(),key=operator.itemgetter(1)) #(1) : 두번째 데이터를 정렬의 기준으로 설정함
print(type(tranList))
print(tranList)

tranList = tranDic.items()
print(type(tranList))
print(tranList)