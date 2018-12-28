'''
Created on 2018. 12. 24.

@author: a
soupex4.py : 람다를 이용한 선택
'''
from bs4 import BeautifulSoup
import urllib.request as req
url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)

soup = BeautifulSoup(res,"html.parser",from_encoding="euc-kr")
hlist = soup.select("div.head_info")
htitle = soup.select("h3.h_lst")
for tag,title in zip(hlist,htitle):
    #tag : div.head_info 태그 한개
    #title : h3,h_lst 태그한개
    print(title.select_one("span.blind").string,end="\t")
    value=tag.select_one("span.value").string
    print(value,end="원\t")
    change = tag.select_one("span.change").string
    print(change,end="\t")
    # tag.select("span.blind") : div.head_info 태그의 span.blind들 선택
    blinds=tag.select("span.blind")
    b = tag.select("span.blind")[len(blinds)-1].string
    print(b,end="********\n")