import matplotlib.pyplot as p
import random as r
import tqdm
s = (2000,2000)
N = 100
I = 100000
G = [[0 for j in range(s[1])]for i in range(s[0])]
def u(p,g):
 X = len(g[0])
 Y = len(g)
 x = p[0]
 y = p[1]
 return [[x+1%X,y],[x-1%X,y],[x,y+1%Y],[x,y-1%Y]]
A=[[[r.randint(0, s[0]),r.randint(0, s[1])]]for x in range(N)]
for i in tqdm.tqdm(range(I)):
 for j in range(N):
  A[j].append(r.choice(u(A[j][-1],G)))
  try:
    G[A[j][-1][1]][A[j][-1][0]]=j+1
  except:
    a=1
p.imshow(G)
print("saving...")
p.savefig('saver.png', dpi=300)