import matplotlib.pyplot as p
a=p.axes(projection='3d')
x=range(0,255,10)
for i in x:
 for j in reversed(x):
  for k in x:
   a.plot([i],[j],[k],color=(i/255.,j/255.,k/255.),markersize=20,marker='o')
p.show()