"""
	fibonaccispiral.py
	
"""	
import matplotlib.pyplot as plt 
import numpy as np
f = [0,1]
for i in range(30):
	f.append(f[-1]+f[-2])
print(f)
x = 0
y = 0
c = 0
i = 0
while (c < f[-1]):
	i+=1
	for j in range(2*i):
		o = (-1)**(i+1)
		c+=1
		if (j//i==0):
			x+=o
		else:
			y+=o
		if c in f:
			plt.plot([x],[y],".",color=(1,0,0),ms=1)
		#else:
		#	plt.plot([x],[y],".",c=(i/f[-1],0,0),ms=2)

plt.grid(True)
#plt.xscale('log')
#plt.yscale('log')
plt.title("Fibonacci spiral; 30 first terms")

plt.show()