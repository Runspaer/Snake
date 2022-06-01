from Controllers.Control import *
from Controllers.Objs.Snake import *


def include_objs():
    #Параметры экрана
    #screen_size = [1280, 800]
    screen_size = [800, 600]


    color=None
    #Russia
    Russia=[(240, 255, 255),(0, 82, 255),(255, 9, 47)]
    color_Russia=[]
    for j in Russia:
        for i in range(10):
            color_Russia.append(j)

    #Bee
    Bee=[(28, 28, 28),(255, 185, 15)]
    color_Bee=[]
    for j in Bee:
        for i in range(5):
            color_Bee.append(j)

    #Жвачка
    color_gum=[(255, 86, 86),(255, 81, 122),(255, 95, 165),(255, 129, 205),(252, 138, 255),(145, 142, 255),
    (102, 158, 255),(145, 142, 255),(252, 138, 255),(255, 129, 205),(255, 95, 165),(255, 81, 122),(255, 86, 86)]

    #Falt
    Falt=[ (212, 223, 255), (172, 187, 255), (78, 104, 255), (172, 187, 255), (212, 223, 255)]
    color_Falt=[]
    for j in Falt:
        for i in range(3):
            color_Falt.append(j)

    mass=[]


    mass.append(Apples_Control([Apple(Physics_regular_polygon(Point(randrange(5, screen_size[0]-5, 20),
                                             randrange(5, screen_size[1]-5)),20,4,'red',1,Point(0,0),0)),Apple(Physics_regular_polygon(Point(randrange(5, screen_size[0]-5, 20),
                                             randrange(5, screen_size[1]-5)),25,5,'red',1.5,Point(1,0),1)),Apple(Physics_regular_polygon(Point(randrange(5, screen_size[0]-5, 20),
                                             randrange(5, screen_size[1]-5)),30,6,'red',2,Point(0,0),0))]))

    # Круглая Змея
    mass.append(Snake_Control1(Snake(Physics_regular_polygon(Point(screen_size[0]//2,screen_size[1]//2),25,16,'green',0,Point(1.5,0),1),Point(5,5),color),Buttons(pygame.K_LEFT,pygame.K_RIGHT)))


    weight=150
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

    mass.append(Apples_Control([],'apples_scene_0_a.csv'))
    mass.append(Walls_Control([],'walls_scene_0.csv'))
    return [mass,screen_size]
