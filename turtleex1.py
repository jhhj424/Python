'''
Created on 2018. 12. 18.
turtleex1.py : GUI 관련 패키지
@author: a
'''

import turtle
import random
from tkinter.simpledialog import *

inStr = ""
swidth, sheight = 300,300
tx, ty, txtsize = [0] * 3

#GUI 윈도우 설정
turtle.title("거북 글자쓰기")
turtle.shape("turtle")
turtle.setup(width=swidth + 50, height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()
inStr = askstring("문자열 입력","거북이가 쓸 문자열을 입력하세요")
for ch in inStr :
    tx = random.randrange(-swidth/2,swidth/2)
    ty = random.randrange(-sheight/2,sheight/2)
    r = random.random() #red
    g = random.random() #green
    b = random.random() #blue
    txtsize = random.randrange(10,50)
    turtle.goto(tx,ty)
    turtle.pencolor((r,g,b))
    turtle.write(ch,font=("맑은고딕",txtsize,"bold"))
turtle.done()