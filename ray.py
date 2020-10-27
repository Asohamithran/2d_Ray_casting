import numpy as np
import p5

class Ray:
    def __init__(self,pos,angle):
        self.pos=pos
        self.dir=p5.Vector.from_angle(angle)        
    def set_dir(self,x,y):
        self.dir.x = x- self.pos.x
        self.dir.y= y-self.pos.y
        self.dir.normalize()


    def show_ray(self):
        p5.push_matrix()
        p5.translate(self.pos.x,self.pos.y)
        p5.stroke(255,160)
        p5.line(0,0,self.dir.x*5,self.dir.y*5)
        p5.stroke_weight(3)
        p5.pop_matrix()  
    def intersect(self,boundary):
        x1= boundary.start.x
        y1= boundary.start.y
        x2= boundary.end.x
        y2= boundary.end.y
        # print(self.pos)
        x3=self.pos.x
        y3=self.pos.y
        x4=self.pos.x+self.dir.x
        y4= self.pos.y+self.dir.y
        # print((x3,y3),(x4,y4))
        den= (x1-x2) * (y3-y4) -(y1-y2)*(x3-x4)   
        if (den ==0):
            return
        else:
            t = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/den
            u= -((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))/den
            if(t>0 and t<1 and u>0):
                #find the point using t and u
               
               pt_x=x1+t*(x2-x1)
               pt_y=y1+t*(y2-y1)
               pt=p5.Vector(pt_x,pt_y)
            #    p5.circle(pt.x,pt.y,4)
            #    print(pt)
               return pt
            else:
                # print(f"false")
                return None   

