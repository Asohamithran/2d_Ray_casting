import numpy as np
import p5
from boundary import Boundary
from ray import Ray
from all_rays import All_rays
import random
global xoff
global yoff
# print(random.randint(3, 9))
xoff=0.0
yoff=1000.0

Boundaries=[]
for j in range(5):
    x1=random.randint(0,width)
    x2=random.randint(0,width)
    y1=random.randint(0,height)
    y2=random.randint(0,height)
    Boundaries.append(Boundary(x1,x2,y1,y2))
Boundaries.append( Boundary(0, 0, width, 0)) 
Boundaries.append( Boundary(width, 0, width, height)) 
Boundaries.append( Boundary(width, height, 0, height)) 
Boundaries.append( Boundary(0, height, 0, 0))      
rays=All_rays(width/2,height/2)
def setup():
    p5.size(400, 400) 
    
     
def draw():
    global xoff,yoff
    p5.background(0)
    for i in Boundaries: 
        i.show_boundary()

    # r.set_dir(mouse_x,mouse_y)
    # r.show_ray()
    rays.update(p5.noise(xoff)*width,p5.noise(yoff)*height)
    # rays.update(mouse_x,mouse_y)
    rays.show()
    rays.look(Boundaries)
    # t=r.intersect(b)
    xoff+=0.01
    yoff+=0.01
    # print(xoff,yoff)
p5.run()

