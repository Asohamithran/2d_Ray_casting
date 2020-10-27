import numpy as np
import p5
from boundary import Boundary
from ray import Ray
# from all_rays import All_rays
class All_rays():
    def __init__(self,a,b):
        self.pos= p5.Vector(a,b)
        self.rays=[]
        print(self.pos.x,self.pos.y)
        for a in range(0,360,9):
            self.rays.append(Ray(self.pos,p5.radians(a)))

        return 
    def update(self,x,y):
        self.pos.x=x
        self.pos.y=y               
    def show(self):
        for r in self.rays:
            r.show_ray()
    def look(self,walls):
        
        for r in self.rays:
            closest_point =None
            max_distance=9e9 
            for i in walls : 
                ptr=r.intersect(i)
                if(ptr!=None):
                    d=p5.Vector.dist(self.pos,ptr)
                    if (d<max_distance):
                        max_distance=d
                        closest_point=ptr 
            if(closest_point!=None):
                p5.stroke(255,90)
                p5.line(self.pos.x,self.pos.y,closest_point.x,closest_point.y)

        