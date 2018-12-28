'''
Created on 2018. 12. 18.

@author: a

exam10.py :
            c:/Windows/win.ini 파일을 읽어서
            c:/temp/win.bak 파일에 복사하기
'''

read = None
write = None
read = open("c:/Windows/win.ini","r")
write = open("c:/temp/win.bak","w")
msg = ""
for i in read :
    msg += i
write.writelines(msg)
read.close()
write.close()