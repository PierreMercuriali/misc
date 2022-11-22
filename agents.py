import matplotlib.pyplot as plt
import numpy as np
import random, tqdm, math
size          = (200,200)
nbagents      = 20
iterations    = 10000
grid          = [[0 for j in range(size[1])] for i in range(size[0])]

def distance(p1, p2):
    return math.sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def gradient(start, end, l):
    #color gradient
    g = [start]
    xgradientStep = float(end[0] - start[0])/l
    ygradientStep = float(end[1] - start[1])/l
    zgradientStep = float(end[2] - start[2])/l
    for i in range(l):
        g.append([
            min(1, g[-1][0]+xgradientStep),
            min(1, g[-1][1]+ygradientStep),
            min(1, g[-1][2]+zgradientStep)])
    return g

def availableDirections(pos,g):
    #approach directions!
    xMax = len(g[0])-1
    yMax = len(g)-1
    x = pos[0]
    y = pos[1]
    res = []
    if not(x==0):
        res.append([(x-1), (y)])
    if not(y==0):
        res.append([(x), (y-1)])
    if not(x==xMax):
        res.append([(x+1), (y)])
    if not(y==yMax):
        res.append([(x), (y+1)])
    
    #add filter if not random
    filtered = []
    for point in res:
        filtered.append(point)
        try:
            t = g[point[1]][point[0]]
        except:
            print(point)
        if not (g[point[1]][point[0]]==0):#attraction to paths
            filtered.append(point)
    return filtered
    if filtered==[]:
        return res
    else:
        return res#filtered

def availableDirectionsTorus(pos,g):
    #approach directions!
    xMax = len(g[0])
    yMax = len(g)
    x = pos[0]
    y = pos[1]
    res = [
        [(x+1)%xMax, (y)%yMax],
        [(x-1)%xMax, (y)%yMax],
        [(x)%xMax, (y+1)%yMax],
        [(x)%xMax, (y-1)%yMax]
        ]
    
    #add filter if not random
    filtered = []
    for point in res:
        filtered.append(point)
        if not (g[point[1]][point[0]]==0): 
            filtered.append(point)
            filtered.append(point)
            filtered.append(point)
            filtered.append(point)
    return filtered
    if filtered==[]:
        return res
    else:
        return res#filtered
    
def availableDirectionsAvoid(pos,g):
    xMax = len(g[0])
    yMax = len(g)
    x = pos[0]
    y = pos[1]
    res = [
        [(x+1)%xMax, (y)%yMax],
        [(x-1)%xMax, (y)%yMax],
        [(x)%xMax, (y+1)%yMax],
        [(x)%xMax, (y-1)%yMax]
        ]
    
    #add filter if not random
    filtered = []
    for point in res:
        if g[point[1]][point[0]]==0:
            filtered.append(point)
    if filtered==[]:
        return [pos]
    else:
        return filtered


savecode = "".join([random.choice("1234567890") for i in range(16)])

#agents starting position
agents = [[[random.randint(0, size[0]), random.randint(0, size[1])]] for x in range(nbagents)]
distances = [[] for i in range(nbagents)]
print("Computing paths...")
for i in tqdm.tqdm(range(iterations)):
    for j in range(nbagents):
        #choose a direction
        d = availableDirections(agents[j][-1], grid)
        #move agent at random
        agents[j].append(random.choice(d))
        #update grid
        grid[agents[j][-1][1]][agents[j][-1][0]] = j + 1
    #compute distances between agents:
    for j in range(nbagents):
        distances[j].append(  distance( [0,0], agents[j][-1] )  )
        
print("Displaying grid...")        
plt.imshow(grid)
print("Saving grid...")
plt.savefig(savecode+"agents.png", dpi=200)
plt.show()
plt.clf()
print("Displaying agent distances...")
for i in range(nbagents):
    plt.plot(distances[i], color = (.7,.7,.7),linestyle='solid', linewidth=.5)
#    plt.scatter(distances[i], list(range(len(distances[i]))), color = (.7,.7,.7),marker='.', markersize=.5)

plt.savefig(savecode+"agentsorigindistances.png", dpi=200)
plt.show()
    
    