'''
Created on 2018. 12. 24.

@author: a
soupex4.py : 람다를 이용한 선택
'''
from bs4 import BeautifulSoup
fp = open("books.html",encoding="utf-8")
soup = BeautifulSoup(fp,"html.parser") #파일 정보도 BeautifulSoup 객체로 이용가능
#람다식을 이용하여 출력하기
sel = lambda q : print(soup.select_one(q).string)
sel("#nu")                  #전체 페이지에서 id="nu" 태그를 선택
sel("li#nu")                # li 태그 중 id="nu" 태그를 선택
sel("ul > li#nu")           # ul 태그의 하위태그중 li 태그 중 id="nu" 태그를 선택
sel("#bible #nu")           # id="bible" 인 태그의 하위 태그 중 id="nu"인 태그를 선택
sel("#bible > #nu")         # id="bible" 인 태그의 하위 태그 중 id="nu"인 태그를 선택
sel("ul#bible > li#nu")
sel("li[id='nu']")          # li 태그 중 id 속성의 값이 nu인 태그를 선택
sel("li:nth-of-type(4)")    # li 태그 중 4번째 인 태그를 선택

#기타 방식으로 출력하기
print(soup.select("li")[3].string)
print(soup.find_all("li")[3].string)