import pygame

from another.Controllers.Control import *
from another.Controllers.Objs.Snake import *


def include_objs():
    #Параметры экрана
    screen_size = [1280, 960]



    mass=[]
    speed = Point(randint(-200, 200), randint(-10, 10))
    speed = speed * (1 / speed.abs()) * 3

    # Квадратная
    # mass.append(Snake_Control1(Snake(Physics_polygon(Point(screen_size[0]//2+20,screen_size[1]//2+40),[Point(-10,10)*2,Point(10,10)*2,Point(10,-10)*2,Point(-10,-10)*2]
    #                                                 ,'green',1,speed,0),Point(550,5)),Buttons(pygame.K_LEFT,pygame.K_RIGHT)))

    #Круглая Змея
    # mass.append(Snake_Control1(Snake(Physics_regular_polygon(Point(screen_size[0]//2,screen_size[1]//2),40,16,'red',3,speed,0),Point(550,5)),Buttons(pygame.K_LEFT,pygame.K_RIGHT)))

    # Фигура 1
    # AstapoTraideR=[Point(3,2),Point(6,0),Point(5,-3),Point(-5,-3),Point(-6,0),Point(-3,2)]
    # for i in range(len(AstapoTraideR)):
    #     AstapoTraideR[i]=AstapoTraideR[i]*-7
    # mass.append(Snake_Control1(Snake(Physics_polygon(Point(100,100),AstapoTraideR
    #                                                  , (0, 255, 0), 2, speed, 0),
    #                                   Point(550,5)), Buttons(pygame.K_LEFT, pygame.K_RIGHT)))

    # cat snake and cat wall
    # cat_head=[Point(2, 3), Point(4, 5), Point(6, 3),Point(6, -1),Point(3, -3),Point(-3, -3),Point(-6, -1),Point(-6, 3),Point(-4, 5),Point(-2,3)]
    # for i in range(len(cat_head)):
    #     cat_head[i]=cat_head[i]*-5
    # mass.append((Walls_Control(Wall(Physics_polygon(Point(300,200),cat,(0, 255, 0), 0, Point(0, 0), 0)))))

    # mass.append(Snake_Control1(Snake(Physics_polygon(Point(100,100),cat_head
    #                                                  , (0, 255, 0), 1, Point(2, 0), 0),
    #                                   Point(550,5)), Buttons(pygame.K_v, pygame.K_b)))

    cat = [Point(1, 1), Point(4, 1), Point(4, 3), Point(3, 3), Point(3, 4), Point(5, 4), Point(5, -4),
            Point(4, -4), Point(4, -2), Point(3, -2),Point(3, -4),Point(2, -4),Point(2, -1),Point(0, -1),
           Point(0, -4),Point(-1, -4),Point(-1, -2),Point(-2, -2),Point(-2, -4),Point(-3, -4),Point(-3, 0)
           ,Point(-5, 1),Point(-5, 3),Point(-4, 4),Point(-3, 3),Point(-1, 3),Point(0, 4),Point(1, 3)]
    for i in range(len(cat)):
        cat[i] = cat[i] * -10
    #
    mass.append(Snake_Control1(Snake(Physics_polygon(Point(100, 100), cat
                                                     , (0, 255, 0), 1, speed, 0),
                                     Point(550, 5)), Buttons(pygame.K_v, pygame.K_b)))




















    side=30
    mass.append(Walls_Control(Wall(Physics_polygon(Point(0, screen_size[1] / 2),
                                                    [Point(side, side*3), Point(side, -side*3), Point(-side, -side*3),Point(-side, side*3)],
                                                    'blue', 1, Point(0, -2), 0)),Buttons(pygame.K_w,pygame.K_s)))
    mass.append(Walls_Control(Wall(Physics_polygon(Point(screen_size[0], screen_size[1] / 2),
                                                   [Point(side, -side*3), Point(side, side*3), Point(-side, side*3),Point(-side, -side*3)],
                                                   'blue', 1, Point(0, -2), 0)),Buttons(pygame.K_UP,pygame.K_DOWN)))

    #cat
    # mass.append(Walls_Control(Wall(Physics_polygon(Point(0, screen_size[1] / 2), cat
    #                                                  , (0, 255, 0), 1, Point(0, -2), 0)), Buttons(pygame.K_v, pygame.K_b)))



















    weight=150
    mass.append(Walls_Control([Wall(Physics_polygon(Point(screen_size[0]/2, -weight),
                                                   [Point(screen_size[0]/2, -weight), Point(screen_size[0]/2, weight),
                                                    Point(-screen_size[0]/2, weight), Point(-screen_size[0]/2, weight)],
                                                   'blue', 0, Point(0, 0), 0)),Wall(Physics_polygon(Point(screen_size[0] / 2, screen_size[1]+weight),
                                                   [Point(screen_size[0] / 2, weight), Point(screen_size[0] / 2, -weight-1),
                                                    Point(-screen_size[0] / 2, -weight-1), Point(-screen_size[0] / 2, weight)],
                                                   'blue', 0, Point(0, 0), 0))]))#Все игровые стены
    # mass.append(Apples_Control([Apple(Physics_regular_polygon(Point(50,50),10,3,'red',0,Point(0,0),0)),Apple(Physics_regular_polygon(Point(100,100),30,16,'red',0,Point(0,0),0))]))

    return [mass,screen_size]
