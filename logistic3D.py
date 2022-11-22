"""
	logistic.py
	Displays a logistic map in very few lines of code
	
"""	
import matplotlib.pyplot as plt 
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for m in np.arange(1,30):
	print(m)
	data = []
	for r in np.arange(3,3.5,.1):
		for x in np.arange(0,1,.1):
			for i in range(m):
				x = r * x * (1 - x)
				if ((r,x) in data):
					break
				else:
					plt.plot([r],[x],[m],".",c=(x,0,0),ms=2)#,alpha=.5)
					data.append((r,x))


plt.grid(True)
plt.title("logistic map x <- r * x (1 - x), 1 to 10 iterations")
plt.xlabel("r")
plt.ylabel("x (initial)")
#plt.zlabel("number of iterations")
plt.show()