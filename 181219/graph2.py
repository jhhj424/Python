'''
Created on 2018. 12. 19.

@author: a

graph2.py
'''
#numpy : python의 수치계산용 배열.
import numpy as np ## pip3 install numpy
import matplotlib.pyplot as plt ## pip3 install ggplot

plt.style.use("ggplot")
N = 500
# 정규화 에 맞도록 난수를 발생함. 임의로 수치를 저장. 그래프를 그리기 위한 수치를 생성
normal = np.random.normal(loc=0.0, scale=1.0, size=N)
lognormal = np.random.lognormal(mean=0.0, sigma=1.0, size=N)
index_value = np.random.random_integers(low=0, high=N-1, size=N)
normal_sample = normal[index_value]
lognormal_sample = lognormal[index_value]

bax_plot_data = [normal,normal_sample,lognormal,lognormal_sample]

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
box_labels = ['normal','normal sample','lognormal','lognormal_sample']
# boxplot : 최대값, 최소값, 편차 등을 그래프로 표시
ax1.boxplot(bax_plot_data, notch=False, sym='.',vert=True,whis=1.5,
            showmeans=True,labels=box_labels)
ax1.xaxis.set_ticks_position("bottom")
ax1.yaxis.set_ticks_position("left")
ax1.set_title("Box Plot")
ax1.set_xlabel("Distribution")
ax1.set_ylabel("Value")

plt.savefig("box_blot.png",dpi=400,bbox_inches="tight")
plt.show()