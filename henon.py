import matplotlib.pyplot as plt 
import numpy as np
import math
plt.rcParams['axes.facecolor'] = (.5,.5,.5)
a = 1.4
b = .3
fig = plt.figure()
ax = fig.add_subplot(projection='3d')


data = []
for m in range(1,20):
	for x in np.arange(-2,2,.03):
		for y in np.arange(-2,2,.02):
			for i in range(m):
				nx = 1 - a * x * x + y
				y = b * x
				x = nx
				if abs(x)>100:
					break
			if abs(x)<2 and abs(y)<2:
				plt.plot([x],[y],[m],".",color = (abs(x)/2,0,abs(y)/2), ms=2)
	


plt.grid(True)
#plt.title("logistic map x <- r * x (1 - x), 50 iterations")
#plt.xlabel("r")
#plt.ylabel("x (initial)")
plt.show()