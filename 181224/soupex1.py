'''
Created on 2018. 12. 24.

@author: a

soupex1.py : 크롤링하기
'''
from bs4 import BeautifulSoup # pip3 install beautifulsoup4
import urllib.request as req

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser")
title = soup.find("title").string

wf = soup.find("wf").string
print(title)
print(wf)