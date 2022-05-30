import pygame

from Controllers.Control import *
from Controllers.Objs.Snake import *


def include_objs():
    #Параметры экрана
    #screen_size = [1280, 800]
    screen_size = [800, 600]


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
    color=[(255, 86, 86),(255, 81, 122),(255, 95, 165),(255, 129, 205),(252, 138, 255),(145, 142, 255),
    (102, 158, 255),(145, 142, 255),(252, 138, 255),(255, 129, 205),(255, 95, 165),(255, 81, 122),(255, 86, 86)]

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

    mass=[]

    # for i in range(5):
    #     # mass.append(Apples_Control([Apple(Physics_circle(Point(50, 50), 30, 16, 'red', 0, Point(0, 0), 0)),
    #     #                             Apple(Physics_circle(Point(50, 50), 30, 16, 'red', 0, Point(0, 0), 0))]))
    #
    #     mass.append(Apples_Control([Apple(Physics_circle(Point(50,50),10,3,'red',0,Point(0,0),0)),Apple(Physics_circle(Point(50,50),10,6,'red',0,Point(0,0),0))]))
    # mass.append(Apples_Control(Apple(Physics_polygon(Point(50,50), [Point(-10,10),Point(10,10),Point(10,-10),Point(-10,-10)],'red',0,Point(0,0),0))))


    # mass.append(Snake(Physics_circle(Point(screen_size[0]//2,screen_size[1]//2),[Point(15,0)],'green'),Point(2,0)))
    # mass.append(Apple(Physics_circle(Point(50,50),[Point(10,0)],'red'),Point(0,0)))
    # circle Snake
    # mass.append(Snake_Control1(Snake(Physics_circle(Point(screen_size[0]//2,screen_size[1]//2),[Point(15,0)]
    #                                                   ,'green',0,Point(5,0),5),Point(5,5)),Buttons(pygame.K_LEFT,pygame.K_RIGHT)))

    # Астапкин
    # AstapoTraideR=[Point(3,2),Point(6,0),Point(5,-3),Point(-5,-3),Point(-6,0),Point(-3,2)]
    # for i in range(len(AstapoTraideR)):
    #     AstapoTraideR[i]=AstapoTraideR[i]*-7
    # mass.append(Snake_Control1(Snake(Physics_polygon(Point(100,100),AstapoTraideR
    #                                                  , (0, 255, 0), 1, Point(5, 0), 1),
    #                                   Point(420, 5), color), Buttons(pygame.K_LEFT, pygame.K_RIGHT)))



    # Квадратная
    # mass.append(Snake_Control1(Snake(Physics_polygon(Point(screen_size[0]//2,screen_size[1]//2),[Point(-10,10)*2,Point(10,10)*2,Point(10,-10)*2,Point(-10,-10)*2]
    #                                                 ,'green',0.5,Point(2,0),1.5),Point(5,5)),Buttons(pygame.K_LEFT,pygame.K_RIGHT)))

    #Кривая квадратная змея
    # sq=[Point(-20, 20), Point(6, 20), Point(6, -20), Point(-20, -20)]
    # for i in range(len(sq)):
    #     sq[i]=sq[i]*2
    # mass.append(Snake_Control1(Snake(Physics_polygon(Point(screen_size[0] // 2, screen_size[1] // 2),sq
    #
    #                                                  , 'green', 1, Point(2, 0), 2), Point(10, 450),colorR),
    #                            Buttons(pygame.K_LEFT, pygame.K_RIGHT)))

    # triangle Snake и круг
    # a=Point(0,0)
    # b=Point(0,0)
    # a.x,a.y=np.dot(np.array([[np.cos(np.radians(120)),-np.sin(np.radians(120))],[np.sin(np.radians(120)),np.cos(np.radians(120))]],float),np.array([0,-10],float))
    # b.x,b.y=np.dot(np.array([[np.cos(np.radians(120)),np.sin(np.radians(120))], [-np.sin(np.radians(120)), np.cos(np.radians(120))]],float),np.array([0,-10],float))
    # mass.append(Snake_Control1([Snake(Physics_polygon(Point(randrange(5, screen_size[0]-5, 20),
    #                                          randrange(5, screen_size[1]-5)),
    # [Point(0, -10), a, b],(0,255,0),1, Point(4, 0),2),Point(420,5),Russia),Snake(Physics_circle(Point(50,50),20,8,'red',1,Point(2,0),2),Point(5,5),color)],Buttons(pygame.K_v,pygame.K_b)))

    # a=a*5
    # b=b*5
    # mass.append(Snake_Control1(Snake(Physics_polygon(Point(100,100),
    #                                                   [Point(0, -10), a, b], (0, 255, 0), 10, Point(2, 0), 1),
    #                                   Point(420, 5), colorR), Buttons(pygame.K_v, pygame.K_b))) # пойдёт для одной из сцен


    # cat snake and cat wall
    # cat=[Point(2, 3), Point(4, 5), Point(6, 3),Point(6, -1),Point(3, -3),Point(-3, -3),Point(-6, -1),Point(-6, 3),Point(-4, 5),Point(-2,3)]
    # for i in range(len(cat)):
    #     cat[i]=cat[i]*-5
    # mass.append((Walls_Control(Wall(Physics_polygon(Point(300,200),cat,(0, 255, 0), 0, Point(0, 0), 0)))))
    # mass.append(Snake_Control1(Snake(Physics_polygon(Point(100,100),cat
    #                                                  , (0, 255, 0), 1, Point(2, 0), 1),
    #                                   Point(420, 5), color), Buttons(pygame.K_v, pygame.K_b)))

    #star snake и star wall
    star=[Point(0, 4), Point(0, -4), Point(0, 0),Point(4, 0),Point(-4, 0), Point(0, 0)]
    for i in range(len(star)):
        star[i]=star[i]*-8
    # mass.append((Walls_Control(Wall(Physics_polygon(Point(100,100),star,(0, 255, 0), 0, Point(0, 0), 0)))))
    mass.append(Snake_Control1(Snake(Physics_polygon(Point(100,100),star
                                                     , (0, 255, 0), 1, Point(5, 0), 1),
                                      Point(420, 5), colorR), Buttons(pygame.K_v, pygame.K_b)))



    #Круглая Змея
    # mass.append(Snake_Control1(Snake(Physics_circle(Point(50,50),20,16,'red',0,Point(3,0),2),Point(5,5),color),Buttons(pygame.K_LEFT,pygame.K_RIGHT)))




    # size=20
    # center=[Point(300, 200),Point(100, 400),Point(200, 430)]
    # triangle=[1,1.5,1]
    # for i in range(len(center)):
    #     mass.append(Walls_Control(Wall(Physics_polygon(center[i],
    #                                                [Point(-size, size),
    #                                                 Point(-size, -size),
    #                                                 Point(size, -size),
    #                                                 Point(size, size)],
    #                                                'blue', triangle[i], Point(1, 0), triangle[i]))))# двигающийся прямоугольник
    # mass.append(Walls_Control(Wall(Physics_polygon(Point(100,200),
    #                                                [Point(-size, size),
    #                                                 Point(-size, -size),
    #                                                 Point(size, -size),
    #                                                 Point(size, size)],
    #                                                'blue', 1, Point(0, 0), 0))))


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
    weight=300
    mass.append(Walls_Control([Wall(Physics_polygon(Point(-weight, screen_size[1] / 2),
                                                    [Point(weight, screen_size[1] / 2), Point(weight, -screen_size[1] / 2), Point(-weight, -screen_size[1] / 2),Point(-weight, screen_size[1] / 2)],
                                                    'blue', 0, Point(0, 0), 0)),Wall(Physics_polygon(Point(screen_size[0]+weight, screen_size[1] / 2),
                                                   [Point(weight, -screen_size[1] / 2), Point(weight, screen_size[1] / 2), Point(-weight-1, screen_size[1] / 2),Point(-weight-1, -screen_size[1] / 2)],
                                                   'blue', 0, Point(0, 0), 0)),Wall(Physics_polygon(Point(screen_size[0]/2, -weight),
                                                   [Point(screen_size[0]/2, -weight), Point(screen_size[0]/2, weight),
                                                    Point(-screen_size[0]/2, weight), Point(-screen_size[0]/2, weight)],
                                                   'blue', 0, Point(0, 0), 0)),Wall(Physics_polygon(Point(screen_size[0] / 2, screen_size[1]+weight),
                                                   [Point(screen_size[0] / 2, weight), Point(screen_size[0] / 2, -weight-1),
                                                    Point(-screen_size[0] / 2, -weight-1), Point(-screen_size[0] / 2, weight)],
                                                   'blue', 0, Point(0, 0), 0))]))#Все игровые стены

    # mass.append(Apples_Control([],'apples_scene_1.csv'))
    mass.append(Walls_Control([],'walls_scene_2.csv'))
    return [mass,screen_size]
