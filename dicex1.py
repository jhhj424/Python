'''
Created on 2018. 12. 18.
dicex1.py : 딕셔너리 예제2
@author: a
'''

foods = {"떡볶이" : "오뎅" , "짜장면":"단무지", "라면":"김치","피자":"피클","맥주":"땅콩","치킨":"치킨무","삼겹살":"상추"}
while True :
    myfood = input(str(list(foods.keys())) + "중 좋아하는 음식은?")
    if myfood in foods :
        print("<%s> 궁합 음식은 <%s> 입니다." % (myfood,foods.get(myfood)))
    elif myfood == "끝" : # foods의 모든 내용을 출력하기
        for i in foods.keys() :
            print("%s => %s" % (i,foods[i]), end=",")
        break
    else :
        print("그런 음식은 없습니다.")
        yn = input("좋아하는 음식으로 저장 하시겠습니까*(y/n)?")
        if yn == 'y' :
            f = input("궁합음식은 무엇입니까?")
            foods[myfood] = f