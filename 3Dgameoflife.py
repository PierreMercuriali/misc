import matplotlib.pyplot as p
import random
a=p.axes(projection='3d')

xmax = 15
ymax = 15
tmax = 20
#initialize grid
grid = [[random.choice([0,1]) for x in range(xmax)] for y in range(ymax)]

#neighborhood
def neighborhood(x,y,g):
    global xmax, ymax
    return [
            g[(y+1) % ymax][(x) % xmax],
            g[(y+1) % ymax][(x+1) % xmax],
            g[(y+1) % ymax][(x-1) % xmax],
            g[(y) % ymax][(x+1) % xmax],
            g[(y) % ymax][(x-1) % xmax],
            g[(y-1) % ymax][(x) % xmax],
            g[(y-1) % ymax][(x+1) % xmax],
            g[(y-1) % ymax][(x-1) % xmax]
        ]

#update grid
def update(g):
    global xmax, ymax
    new = [[0 for x in range(xmax)] for y in range(ymax)]
    for y in range(ymax):
        for x in range(xmax):
            if g[y][x] == 1: #live cell
                if sum(neighborhood(x,y,g)) in [2,3]:
                    new[y][x] = 1
                else:
                    new[y][x] = 0
            else:
                if sum(neighborhood(x,y,g)) in [3]:
                    new[y][x] = 1
    return new

for t in range(tmax):
    for y in range(ymax):
        for x in range(xmax):
            if grid[y][x] == 1:
                a.plot([x],[y],[t],color=(1 - t/tmax,0,0,.2),markersize=3,marker='o')
    grid = update(grid)
    
p.show()