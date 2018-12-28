'''
Created on 2018. 12. 24.

@author: a
urlex1.py : ip로 결과 출력하기
'''
import urllib.request
url = "http://api.aoikujira.com/ip/ini"
#url = "https://www.naver.com/"
res = urllib.request.urlopen(url) #url 연결하여 응답 정보 저장
data = res.read()
text = data.decode("utf-8")
print(text)