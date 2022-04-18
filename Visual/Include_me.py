from Objs import *
from Objs.Plane.Point import *
def include_objs(screen_size:list):
    mass=[]
    mass.append(Snake.Snake(Point(screen_size[0]//2,screen_size[1]//2),Point(1,0),'green',15,[]))
    mass.append(Apple.Apple(Point(50,50),Point(0,0),'red',10))
    mass.append(Obj.Size_wall(Point(1,screen_size[1]/2),Point(0,0),'blue',0,screen_size[1]/2-1,Point(1,0)))#Левая стена
    mass.append(Obj.Size_wall(Point(screen_size[0]-1, screen_size[1] / 2), Point(0, 0), 'blue', 0, screen_size[1] / 2-1,Point(0,0)))#Правая стена
    mass.append(Obj.Size_wall(Point(screen_size[0]/2, 1), Point(0, 0), 'blue', screen_size[0] / 2, 0,Point(0,1)))#Верхняя стена
    mass.append(Obj.Size_wall(Point(screen_size[0] / 2, screen_size[1]-1), Point(0, 0), 'blue', screen_size[0] / 2, 0,Point(0,0)))#Нижняя стена
    return mass
