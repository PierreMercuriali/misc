import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

WIDTH					= 50
HEIGHT					= 50
SPEED					= 1 #number of pixels particule can "jump" in one tick
NUMBER_OF_PARTICLES		= 20

#data = []
#for i in range(WIDTH):
#	line = []
#	for j in range(HEIGHT):
#		line.append(0.)
#	data.append(line)

fig, ax0 	= plt.subplots(1, 1)
ax0 		= plt.axis([0, WIDTH, 0, HEIGHT])

dots 		= []
dotsData	= []
for i in range(NUMBER_OF_PARTICLES):
	dotsData.append([np.random.randint(WIDTH), np.random.randint(HEIGHT)]) #x, y, color
	
for i in range(NUMBER_OF_PARTICLES):
	dot, 		= plt.plot(dotsData[i][0:1], 'o', color = (np.random.rand(),0,0))#color = dotsData[i][2])
	dots.append(dot)

def update(d):
	global dots
	for i in range(len(d)):
		current_particle 	= d[i]
		neighborhood_size 	= 3
		neighborhood		= []
		for j in range(neighborhood_size):
			for k in range(neighborhood_size):
				for cell in [
								[d[i][0]-j,d[i][1]-k],
								[d[i][0]-j,d[i][1]+k],
								[d[i][0]-j,d[i][1]],
								[d[i][0]+j,d[i][1]-k],
								[d[i][0]+j,d[i][1]+k],
								[d[i][0]+j,d[i][1]],
								[d[i][0],d[i][1]-k],
								[d[i][0],d[i][1]+k],
								[d[i][0],d[i][1]]
							]:
					if cell in d and not(cell in neighborhood):
						neighborhood.append(cell)
		#BROWNIAN MOVEMENT
		r = len(neighborhood)
		if r > .5:
			if np.random.rand()<.1:
				d[i][0] = d[i][0] + ( np.random.choice([-1, 1])*SPEED) 			#% WIDTH
				d[i][1] = d[i][1] + ( np.random.choice([-1, 1])*SPEED) 			#% HEIGHT
			if np.random.rand()<.01:
				d.append([d[i][0], d[i][1]])#a new particle is born!
				dot, = plt.plot(d[i][0], d[i][0],'.', color = (np.random.rand(),.5,.5))
				dots.append(dot)
		else:
			if np.random.rand()<.01:
				d[i][0] = d[i][0] + ( np.random.choice([-1, 1])*SPEED) 			#% WIDTH
				d[i][1] = d[i][1] + ( np.random.choice([-1, 1])*SPEED) 			#% HEIGHT
	return d

def animate(i):
	global dotsData
	dotsData = update(dotsData)
	for i in range(len(dotsData)):
		dots[i].set_data(dotsData[i][0], dotsData[i][1])#, dotsData[i][2] )
	return dots
	
myAnimation = animation.FuncAnimation(fig, animate, frames=20, interval=10, blit=True, repeat=True)

plt.show()