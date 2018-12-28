'''
Created on 2018. 12. 19.

@author: a

graph1.py : 그래프 그리기
'''

import matplotlib.pyplot as plt ##pip3 - r에서 install패키지랑 같은 느낌 / pip3 install ggplot
plt.style.use("ggplot")
customers = ["JAVA","JSP","SPRING","HADOOP","PYTHON"] ##리스트
customers_index = range(len(customers)) ## type : range ## 범위변수// 0 ~ 4 까지의 값
sale_amounts = [65,90,85,60,95] ## 정수값 리스트로 지정

fig = plt.figure() # 그래프를 생성할 공간
ax1 = fig.add_subplot(1,1,1) # 1행 1열 1번째 그래프
#막대그래프
ax1.bar(customers_index,sale_amounts,align="center", color="darkblue")
ax1.xaxis.set_ticks_position("bottom")
ax1.yaxis.set_ticks_position("left")
plt.xticks(customers_index, customers,rotation=0, fontsize="small")

plt.xlabel("Subject")
plt.ylabel("Score")
plt.title("Class Score")

plt.savefig("bar_plot.png",dpi=400,bbox_inches="tight")
plt.show()