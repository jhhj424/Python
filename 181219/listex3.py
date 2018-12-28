'''
Created on 2018. 12. 19.

@author: a
listex3.py 
'''

foods = ['떡볶이','짜장면','라면']
sides = ['오뎅','단무지','김치']
for food,side in zip(foods,sides) :
    print(food,'-->',side)

#두개의 리스트를 튜플의 리스트 객체로 생성
tupList = list(zip(foods,sides))
print(tupList)
#두개의 리스트를 딕셔너리 객체로 생겅
dic = dict(zip(foods,sides))
print(dic)