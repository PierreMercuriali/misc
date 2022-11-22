#average distance between two points in a segment

import matplotlib.pyplot as plt
import random

def d(x,y):
    return abs(x-y)

data = []
lens = []
averages = []
m = 1000


for i in range(m):
    x1 = random.random()
    x2 = random.random()
    data.append([x1,x2])
    lens.append(d(x1, x2))
    a = sum(lens)/len(lens)
    averages.append(a)


#sort data
data = sorted(data, key=lambda k: d(k[0], k[1]))
for i,k in enumerate(data):
    plt.plot([i,i],k, linewidth=.5, color='lightgreen')
    plt.plot([i,i],[0, d(*k)], linewidth=.1, color='darkgreen')
plt.plot(averages, linewidth=.5, color='red')


plt.show()




