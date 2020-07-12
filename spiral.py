import turtle as t
import time as ti
from itertools import cycle

colors=cycle(['red','blue','yellow','green','orange','grey','purple','pink'])
def circle(size,angle,forw):
	t.pencolor(next(colors))
	t.circle(size)
	t.right(angle)
	t.forward(forw)
	circle(size+5,angle+1,forw+5)

t.bgcolor('black')
t.speed('slow')
t.pensize(4)
circle(30,0,1)

ti.sleep(2)
t.hideturtle()