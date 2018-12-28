'''
Created on 2018. 12. 18.
fileex2.py : 콘솔에 입력된 내용을 파일에 쓰기
@author: a
'''

outfp = None
outfp = open("c:/temp/data2.txt","w")
while True :
    outStr = input("내용 입력:")
    if outStr != "" :
        outfp.writelines(outStr + "\n")
    else :
        break
outfp.close()
print("프로그램 종료")