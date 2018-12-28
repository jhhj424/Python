'''
Created on 2018. 12. 24.

@author: a
'''
from bs4 import BeautifulSoup # pip3 install beautifulsoup4
import urllib.request as req

url = "https://finance.naver.com/marketindex/"

res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser",from_encoding="euc-kr")
usd = soup.select_one("div.head_info > span.value").string
print("usd/krw=",usd,end="")
krw = soup.select_one("div.head_info > span.txt_krw > span.blind").string
print(krw)
blind = soup.select_one("div.head_info > span.blind").string
print("변동=",blind)
a = soup.select("div.head_info")
for i in a:
    print(i)