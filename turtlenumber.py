from turtle import *
import math
def build_digits(n, d):
	r = []
	for i in range(1, d):
		r.append(int( str (int(  n * i * 10 ))[-1] ))
	return r
	
	
PATHLEN = 1000	
digits = build_digits( 1228./1298,  PATHLEN)  #( math.exp(1),  PATHLEN)

print(digits)

color('black', 'yellow')

hideturtle()
speed(0)
#begin_fill()
c = 0
for d in digits:
	c+=1
	forward(10)
	right(d*36)
	color( ( float(c)/PATHLEN, 0, 0))
done()
