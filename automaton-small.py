from PIL import Image,ImageDraw
import random as r
m=100
line="".join([r.choice("01")for i in range(m)])
g=Image.new('RGB',(m,m),(0,0,0))
r={"000":"0","001":"1","010":"1","011":"1","100":"1","101":"0","110":"0","111":"0"}
def u(l):
 w=len(l)
 n=""
 for i in range(w):
  n+=r["".join([l[(i-1)%w],l[i],l[(i+1)%w]])]
 return n	
d=[line]		
for i in range(m):
 d.append(u(d[-1]))
for x in range(m):
 for y in range(m):
  if not d[y][x]:
   g.putpixel((x,y),(255,255,255))
g.save('0.png')