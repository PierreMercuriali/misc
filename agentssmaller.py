import matplotlib.pyplot as p
import random as r
X=200;G=[[0 for j in range(X)]for i in range(X)]
def u(p):
 x=p[0];y=p[1]
 return[[x+1%X,y],[x-1%X,y],[x,y+1%X],[x,y-1%X]]
A=[[[0,0]]for x in range(10)]
for i in range(10000):
 for j in range(10):
  A[j].append(r.choice(u(A[j][-1])));G[A[j][-1][1]][A[j][-1][0]]=j+1
p.imshow(G)
p.show()