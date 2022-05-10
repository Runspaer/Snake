import pygame

from Controllers.Control import *
from Controllers.Objs.Snake import *

def include_objs(screen_size:list):
    mass=[]
    mass.append(Apples_Control(Apple(Physics_circle(Point(50,50),[Point(10,0)],'red',0,Point(0,0),0))))
    # mass.append(Snake(Physics_circle(Point(screen_size[0]//2,screen_size[1]//2),[Point(15,0)],'green'),Point(2,0)))
    # mass.append(Apple(Physics_circle(Point(50,50),[Point(10,0)],'red'),Point(0,0)))
    # cquare Snake
    # mass.append(Snake_Control1(Snake(Physics_polygon(Point(screen_size[0]//2,screen_size[1]//2),[Point(-10,10),Point(10,10),Point(10,-10),Point(-10,-10)]
    #                                                  ,'green',1,Point(2,0),5)),Enum(pygame.K_LEFT,pygame.K_RIGHT)))
    # # triangle Snale
    a=Point(0,0)
    b=Point(0,0)
    a.x,a.y=np.dot(np.array([[m.cos(m.radians(120)),-m.sin(m.radians(120))],[m.sin(m.radians(120)),m.cos(m.radians(120))]],float),np.array([0,-10],float))
    b.x,b.y=np.dot(np.array([[m.cos(m.radians(120)),m.sin(m.radians(120))], [-m.sin(m.radians(120)), m.cos(m.radians(120))]],float),np.array([0,-10],float))
    mass.append(Snake_Control1(Snake(Physics_polygon(Point(screen_size[0] // 2, screen_size[1] // 2),
    [Point(0, -10), a, b],'green',1, Point(2, 0),5)),Enum(pygame.K_LEFT,pygame.K_RIGHT)))
    # mass.append(Snake(Physics_polygon(Point(screen_size[0] // 2, screen_size[1] // 2),
    # [Point(0, -10), a, b],'green'), Point(2, 0)))
    # #
    # mass.append(Snake.Snake(Point(screen_size[0]//2,screen_size[1]//2),Point(2,0),'green',15,[]))
    # mass.append(Apple.Apple(Point(50,50),Point(0,0),'red',10))
    #mass.append(Walls_Control(Wall(Physics_polygon(Point(-2,screen_size[1]/2),[Point(1,0),Point(1,screen_size[1]),Point(-1,0),Point(-5,screen_size[1])],'blue',0,Point(0,0),0),Point(1,0))))
    # mass.append(Obj.Size_wall(Point(1,screen_size[1]/2),Point(0,0),'blue',0,screen_size[1]/2-1,Point(1,0)))#Левая стена
    # mass.append(Obj.Size_wall(Point(screen_size[0]-1, screen_size[1] / 2), Point(0, 0), 'blue', 0, screen_size[1] / 2-1,Point(0,0)))#Правая стена
    # mass.append(Obj.Size_wall(Point(screen_size[0]/2, 1), Point(0, 0), 'blue', screen_size[0] / 2, 0,Point(0,1)))#Верхняя стена
    # mass.append(Obj.Size_wall(Point(screen_size[0] / 2, screen_size[1]-1), Point(0, 0), 'blue', screen_size[0] / 2, 0,Point(0,0)))#Нижняя стена
    return mass
