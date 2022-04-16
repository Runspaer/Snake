#from Objs import *
from Obj import *
from Snake import Snake
from Apple import *
def include_objs(screen_size:list):
    mass=[]
    mass.append(Snake(Point(screen_size[0]//2,screen_size[1]//2),Point(1,1),'green',15,[]))
    mass.append(Apple(Point(50,50),Point(0,0),'red',10))
    #mass.append(Size_wall(Point(0,screen_size[1]//2),Point(0,0),'blue',screen_size[1]//2))
    return mass
