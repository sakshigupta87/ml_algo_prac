#!/usr/bin/python3
import matplotlib.pyplot as plt
y=[200,40,60,59]
x=["sam","om","anu","eva"]
y1=[30,50,67,89]
x1=["ss","oo","aa","ee"]
plt.xlabel("time")
plt.ylabel("distance")
#plt.bar(x,y, c='y')
#plt.bar(x1,y1, c='r')
#pltscale(to set scale)
plt.bar(x,y,label="river")
plt.bar(x1,y1,label="railway")
plt.legend()
plt.grid(color='r')
plt.show()
