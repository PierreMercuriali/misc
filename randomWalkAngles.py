import matplotlib.pyplot as plt
import numpy as np
import random, math
import tqdm
iterations = 1000
length = 10 #length of trail tick

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

def availableDirections(pos, r):
    x = pos[0]
    y = pos[1]
    angle = range(0,359)
    return [(x + r*math.cos(2*math.pi*float(a)/360), y + r*math.sin(2*math.pi*float(a)/360)) for a in angle]

def availableDirectionsFilter(pos, r, others):
    #here we avoid others, that are lists of 
    x = pos[0]
    y = pos[1]
    n = 4
    res = []
    for a in range(0,n-1):
        point = (x + r*math.cos(2*math.pi*float(a)/n), y + r*math.sin(2*math.pi*float(a)/n))
        if True:#not collision(segment(pos, point), others):
            res.append(point)
    return res

def segment(p1, p2):
    return [p1, p2]

def distance(p1, p2):
    return math.sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def collision(segment, others):
    for s in others:
        if not intersection(segment, s)==[]:
            return True
    return False

def intersection(s1, s2):
    #intersection of two segments
    res = []
    #points in s2:
    ps1 = [s1[0], s1[1]]
    #points in s2:
    ps2 = [s2[0], s2[1]]    
    for p in ps1:
        for q in ps2:
            if distance(p, q)<6: 
                res.append(p)
    return list(set(res))



#agent starting position
agent1 = [[100,100]]
agent2 = [[150,100]]
agent3 = [[200,100]]
segmentsbut1 = []
segmentsbut2 = []
segmentsbut3 = []
print("Computing paths...")
for i in tqdm.tqdm(range(iterations)):
    #choose a direction
    d1 = availableDirectionsFilter(agent1[-1], length, segmentsbut1)
    d2 = availableDirectionsFilter(agent2[-1], length, segmentsbut2)
    d3 = availableDirectionsFilter(agent3[-1], length, segmentsbut3)
    #move agent at random
    agent1.append(random.choice(d1))
    agent2.append(random.choice(d2))
    agent3.append(random.choice(d3))
    #update segments
    s1 = segment(agent1[-1], agent1[-2])
    s2 = segment(agent2[-1], agent2[-2])
    s3 = segment(agent3[-1], agent3[-2])
    
    segmentsbut1.append(s2)
    segmentsbut1.append(s3)
    segmentsbut2.append(s1)
    segmentsbut2.append(s3)
    segmentsbut3.append(s2)
    segmentsbut3.append(s1)
    

print("Displaying paths...")
a1gradient = gradient((0,0,0), (0,0,0), iterations)
a2gradient = gradient((.3,.3,.3), (.3,.3,.3), iterations)
a3gradient = gradient((.7,.7,.7), (.7,.7,.7), iterations)
for i in tqdm.tqdm(range(iterations-1)):
    p1 = agent1[i]
    p2 = agent1[i+1]
    plt.plot([p1[0], p2[0]],[p1[1], p2[1]], color = (0,0,0),linestyle='solid', linewidth=.5)
    p1 = agent2[i]
    p2 = agent2[i+1]
    plt.plot([p1[0], p2[0]],[p1[1], p2[1]], color = (.3,.3,.3),linestyle='solid', linewidth=.5)
    p1 = agent3[i]
    p2 = agent3[i+1]
    plt.plot([p1[0], p2[0]],[p1[1], p2[1]], color = (.7,.7,.7),linestyle='solid', linewidth=.5)
#add plots at start
plt.plot(*agent1[0], marker="o", color=(0,0,0))
plt.plot(*agent2[0], marker="o", color=(.3,.3,.3))
plt.plot(*agent3[0], marker="o", color=(.7,.7,.7))
plt.axis('off')
#plt.savefig("BIGrandomAnglesNoAvoidance.png", dpi=200)
plt.show()