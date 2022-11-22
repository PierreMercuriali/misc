import matplotlib.pyplot as p 
import numpy as n
d=[]
for r in n.arange(2,4,.05):
 for x in n.arange(0,1,.5):
  for i in range(50):
   x=r*x*(1-x)
   if (r,x) in d:
    break
   else:
    p.plot([r],[x],".",ms=.2,c='r')
    d.append((r,x))
p.show()