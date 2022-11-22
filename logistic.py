"""
	logistic.py
	Displays a logistic map in very few lines of code
	
"""	
import matplotlib.pyplot as plt 
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

data = []
for r in np.arange(2,4,.01):
	print(r)
	for x in np.arange(0,1,.5):
		for i in range(10):
			x = r * x * (1 - x)
			if ((r,x) in data):
				break
			else:
				plt.plot([r],[x],".",c=(0,0,0),ms=2,alpha=.5)
				data.append((r,x))


plt.grid(True)
plt.title("logistic map x <- r * x (1 - x), 50 iterations")
plt.xlabel("r")
plt.ylabel("x (initial)")
plt.show()