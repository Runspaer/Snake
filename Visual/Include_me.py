import pygame

from Controllers.Control import *
from Controllers.Objs.Snake import *

def include_objs(screen_size:list):
    #Координаты многоугольников нужно указывать по часовой стрелке, иначе вы сломаете рисунок
    mass=[]
    mass.append(Apples_Control(Apple(Physics_circle(Point(50,50),[Point(10,0)],'red',0,Point(0,0),0))))
    # mass.append(Snake(Physics_circle(Point(screen_size[0]//2,screen_size[1]//2),[Point(15,0)],'green'),Point(2,0)))
    # mass.append(Apple(Physics_circle(Point(50,50),[Point(10,0)],'red'),Point(0,0)))
    # circle Snake
    # mass.append(Snake_Control1(Snake(Physics_circle(Point(screen_size[0]//2,screen_size[1]//2),[Point(15,0)]
    #                                                   ,'green',0,Point(5,0),5),Point(5,5)),Enum(pygame.K_LEFT,pygame.K_RIGHT)))

    # Квадратная
    # mass.append(Snake_Control1(Snake(Physics_polygon(Point(screen_size[0]//2,screen_size[1]//2),[Point(-10,10),Point(10,10),Point(10,-10),Point(-10,-10)]
    #                                                 ,'green',2,Point(2,0),5),Point(5,5)),Enum(pygame.K_LEFT,pygame.K_RIGHT)))

    #Кривя квадратная змея
    # mass.append(Snake_Control1(Snake(Physics_polygon(Point(screen_size[0] // 2, screen_size[1] // 2),
    #                                                  [Point(-20, 20), Point(6, 20), Point(6, -20), Point(-20, -20)]
    #                                                  , 'green', 3, Point(2, 0), 5), Point(5, 5)),
    #                            Enum(pygame.K_LEFT, pygame.K_RIGHT)))

    # # triangle Snake
    a=Point(0,0)
    b=Point(0,0)
    a.x,a.y=np.dot(np.array([[m.cos(m.radians(120)),-m.sin(m.radians(120))],[m.sin(m.radians(120)),m.cos(m.radians(120))]],float),np.array([0,-10],float))
    b.x,b.y=np.dot(np.array([[m.cos(m.radians(120)),m.sin(m.radians(120))], [-m.sin(m.radians(120)), m.cos(m.radians(120))]],float),np.array([0,-10],float))
    mass.append(Snake_Control1(Snake(Physics_polygon(Point(screen_size[0] // 2, screen_size[1] // 2),
    [Point(0, -10), a, b],'green',3, Point(3, 0),5),Point(5,5)),Enum(pygame.K_LEFT,pygame.K_RIGHT)))

    size=20
    mass.append(Walls_Control(Wall(Physics_polygon(Point(300, 200),
                                                   [Point(-size, size),
                                                    Point(-size, -size),
                                                    Point(size, -size),
                                                    Point(size, size)],
                                                   'blue', 0, Point(0, 0), 5))))# двигающийся прямоугольник
    # mass.append(Snake(Physics_polygon(Point(screen_size[0] // 2, screen_size[1] // 2),
    # [Point(0, -10), a, b],'green'), Point(2, 0)))

    # # #
    # mass.append(Snake.Snake(Point(screen_size[0]//2,screen_size[1]//2),Point(2,0),'green',15,[]))
    # mass.append(Apple.Apple(Point(50,50),Point(0,0),'red',10))
    weight=5
    mass.append(Walls_Control(Wall(Physics_polygon(Point(-weight, screen_size[1] / 2),
                                                    [Point(weight+1, screen_size[1] / 2), Point(weight+1, -screen_size[1] / 2), Point(-weight-1, -screen_size[1] / 2),Point(-weight-1, screen_size[1] / 2)],
                                                    'blue', 0, Point(0, 0), 0))))#Левая стена
    mass.append(Walls_Control(Wall(Physics_polygon(Point(screen_size[0]+weight, screen_size[1] / 2),
                                                   [Point(weight+1, screen_size[1] / 2), Point(weight+1, -screen_size[1] / 2), Point(-weight-1, -screen_size[1] / 2),Point(-weight-1, screen_size[1] / 2)],
                                                   'blue', 0, Point(0, 0), 0))))#Права стена
    mass.append(Walls_Control(Wall(Physics_polygon(Point(screen_size[0]/2, -weight),
                                                   [Point(screen_size[0]/2, -weight-1), Point(screen_size[0]/2, weight+1),
                                                    Point(-screen_size[0]/2, weight+1), Point(-screen_size[0]/2, weight-1)],
                                                   'blue', 0, Point(0, 0), 0))))#Верхняя стена
    mass.append(Walls_Control(Wall(Physics_polygon(Point(screen_size[0] / 2, screen_size[1]+weight),
                                                   [Point(screen_size[0] / 2, weight+1), Point(screen_size[0] / 2, -weight-1),
                                                    Point(-screen_size[0] / 2, -weight-1), Point(-screen_size[0] / 2, weight+1)],
                                                   'blue', 0, Point(0, 0), 0))))
    # mass.append(Obj.Size_wall(Point(1,screen_size[1]/2),Point(0,0),'blue',0,screen_size[1]/2-1,Point(1,0)))#Левая стена
    # mass.append(Obj.Size_wall(Point(screen_size[0]-1, screen_size[1] / 2), Point(0, 0), 'blue', 0, screen_size[1] / 2-1,Point(0,0)))#Правая стена
    # mass.append(Obj.Size_wall(Point(screen_size[0]/2, 1), Point(0, 0), 'blue', screen_size[0] / 2, 0,Point(0,1)))#Верхняя стена
    # mass.append(Obj.Size_wall(Point(screen_size[0] / 2, screen_size[1]-1), Point(0, 0), 'blue', screen_size[0] / 2, 0,Point(0,0)))#Нижняя стена
    return mass
