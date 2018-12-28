'''
Created on 2018. 12. 24.

@author: a
urldownex1.py : url을 이용하여 이미지 down 받아 저장하기
'''
import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
#함수를 이용하여 저장하기
savename = "test.png"
#urllib.request.urlretrieve(url,savename)
#파일을 이용하여 저장하기
mem = urllib.request.urlopen(url).read()
with open(savename,mode="wb") as f :
    f.write(mem)
print("저장완료")