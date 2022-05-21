import pygame

from Controllers.Control import *
from Controllers.Objs.Snake import *

def include_objs(screen_size:list):
    color=None
    #Russia
    Russia=[(240, 255, 255),(0, 82, 255),(255, 9, 47)]
    colorR=[]
    for j in Russia:
        for i in range(5):
            colorR.append(j)

    #Bee
    Bee=[(28, 28, 28),(255, 185, 15)]
    colorBee=[]
    for j in Bee:
        for i in range(5):
            colorBee.append(j)

    #Жвачка
    # color=[(255, 86, 86),(255, 81, 122),(255, 95, 165),(255, 129, 205),(252, 138, 255),(145, 142, 255),
    # (102, 158, 255),(145, 142, 255),(252, 138, 255),(255, 129, 205),(255, 95, 165),(255, 81, 122),(255, 86, 86)]

    #Falt
    # Falt=[ (212, 223, 255), (172, 187, 255), (78, 104, 255), (172, 187, 255), (212, 223, 255)]
    # color=[]
    # for j in Falt:
    #     for i in range(3):
    #         color.append(j)

    #Dead
    # Dead=[(205, 38, 38),(238, 238, 209),(28, 28, 28),(238, 238, 209),(205, 38, 38)]
    # color=[]
    # for j in Dead:
    #     for i in range(3):
    #         color.append(j)







    #Координаты многоугольников нужно указывать по часовой стрелке, иначе вы сломаете рисунок
    mass=[]
    # мем
    for i in range(1):
        mass.append(Apples_Control(Apple(Physics_circle(Point(50,50),[Point(10,0)],'red',0,Point(0,0),0))))


    # mass.append(Snake(Physics_circle(Point(screen_size[0]//2,screen_size[1]//2),[Point(15,0)],'green'),Point(2,0)))
    # mass.append(Apple(Physics_circle(Point(50,50),[Point(10,0)],'red'),Point(0,0)))
    # circle Snake
    # mass.append(Snake_Control1(Snake(Physics_circle(Point(screen_size[0]//2,screen_size[1]//2),[Point(15,0)]
    #                                                   ,'green',0,Point(5,0),5),Point(5,5)),Enum(pygame.K_LEFT,pygame.K_RIGHT)))


    # Квадратная
    # mass.append(Snake_Control1(Snake(Physics_polygon(Point(screen_size[0]//2,screen_size[1]//2),[Point(-10,10),Point(10,10),Point(10,-10),Point(-10,-10)]
    #                                                 ,'green',2,Point(4,0),5),Point(5,5)),Enum(pygame.K_q,pygame.K_a)))

    #Кривая квадратная змея
    mass.append(Snake_Control1(Snake(Physics_polygon(Point(screen_size[0] // 2, screen_size[1] // 2),
                                                     [Point(-20, 20), Point(6, 20), Point(6, -20), Point(-20, -20)]
                                                     , 'green', 0, Point(6, 0), 6), Point(10, 450),colorR),
                               Enum(pygame.K_LEFT, pygame.K_RIGHT)))

    # triangle Snake
    # a=Point(0,0)
    # b=Point(0,0)
    # a.x,a.y=np.dot(np.array([[m.cos(m.radians(120)),-m.sin(m.radians(120))],[m.sin(m.radians(120)),m.cos(m.radians(120))]],float),np.array([0,-10],float))
    # b.x,b.y=np.dot(np.array([[m.cos(m.radians(120)),m.sin(m.radians(120))], [-m.sin(m.radians(120)), m.cos(m.radians(120))]],float),np.array([0,-10],float))
    # mass.append(Snake_Control1(Snake(Physics_polygon(Point(randrange(5, screen_size[0]-5, 20),
    #                                          randrange(5, screen_size[1]-5)),
    # [Point(0, -10), a, b],(0,255,0),3, Point(4, 0),5),Point(420,5),colorBee),Enum(pygame.K_v,pygame.K_b)))

    # Что-то
    # mass.append(Snake_Control1(Snake(Physics_polygon(Point(screen_size[0] // 2, screen_size[1] // 2),
    #             [Point(-20, -5),Point(-10,-11),Point(-5, -20),Point(0, -15), Point(7, 4), Point(0, 15)]
    #             , 'green', 10, Point(8, 0), 6), Point(5, 5),color),
    #             Enum(pygame.K_LEFT, pygame.K_RIGHT)))




    size=20
    center=[Point(300, 200),Point(100, 400),Point(200, 430)]
    triangle=[3,1,2]
    for i in range(len(center)):
        mass.append(Walls_Control(Wall(Physics_polygon(center[i],
                                                   [Point(-size, size),
                                                    Point(-size, -size),
                                                    Point(size, -size),
                                                    Point(size, size)],
                                                   'blue', triangle[i], Point(1, 0), triangle[i]))))# двигающийся прямоугольник


    #
    #Круглая стена
    # mass.append(Walls_Control(Wall(Physics_circle(Point(300, 200),
    #                                                [Point(0,30)],
    #                                                'blue', 0, Point(0, 0), 5))))

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
