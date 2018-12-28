'''
Created on 2018. 12. 18.

@author: a

fileex4.py : 파일관련 함수
'''

import shutil #파일의 복사등 관련 기능을 가진 함수의 모임
import os
import os.path

print(dir(shutil))
print(dir(os))
print(dir(os.path))

#shutil.copy("c:/windows/notepad.exe","c:/temp/note.exe")
print("파일 복사 완료")
#shutil.copytree("c:/temp","c:/temp3") # temp 폴더의 모든 파일을 temp2에 복사하기

'''c:/mydir 폴더 생성하기'''
#os.mkdir("c:/mydir/")#c:에 mydir 폴더 생성하기
'''c:/mydir 폴더 지우기'''
#shutil.rmtree("c:/mydir/")

print("파일의 목록 보기 : os.walk 함수 사용")
for dirName,subDirList,fnames in os.walk("c:\\temp") :
    for fname in fnames :
        print(os.path.join(dirName,fname))