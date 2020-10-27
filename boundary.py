import numpy as np
import p5
class Boundary:
    def __init__(self,x1,y1,x2,y2):
        self.start=p5.Vector(x1,y1)
        self.end=p5.Vector(x2,y2)
    def show_boundary(self):
        p5.line(self.start.x,self.start.y,self.end.x,self.end.y)    
        p5.stroke(255)