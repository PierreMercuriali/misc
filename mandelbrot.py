import matplotlib.pyplot as p
import numpy as n
r=n.arange(-1,1,.01)
d=[]
M=40
for y in r:
    print(y)
    l=[]
    for x in r:
        z=0
        i=0
        while abs(z)<M and i<50:
            i+=1
            z=z*z+x+y*1j
        if abs(z)<M:
            l.append(abs(z)/M)
        else:
            l.append(1)
    d.append(l)
p.imshow(d)
p.show()