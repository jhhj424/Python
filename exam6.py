'''
Created on 2018. 12. 18.
exam6.py : 나라별 수도 정보를 dict 형태로 저장하고, 나라이름을 입력받아 수도를 출력하기.
없는 나라인 경우 dict에 등록할지 여부를 물어 등록하기
나아리음에 "끝" 문자가 입력되면 혀내 등록된 내용을 출력하고 종료하기.
@author: a
'''

country = {}
country["대한민국"] = "서울"
while True :
    ans = str(input("나라이름을 입력하세요"))
    if ans in country :
        print("%s의 수도는 %s 입니다." % (ans, country[ans]))
    elif ans == "끝" :
        for ans in country.keys() :
            print("[%s의 수도:%s]" % (ans,country[ans]),end=" ")
        break
    else :
        yn = str(input("매칭된 수도가 없습니다. 등록하시겠습니까? (y/n)"))
        if yn == "y" :
            country[ans] = str(input("수도이름을 입력하세요"))