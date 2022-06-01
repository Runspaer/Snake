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

    # cat snake and cat wall
    cat_head=[Point(2, 3), Point(4, 5), Point(6, 3),Point(6, -1),Point(3, -3),Point(-3, -3),Point(-6, -1),Point(-6, 3),Point(-4, 5),Point(-2,3)]
    for i in range(len(cat_head)):
        cat_head[i]=cat_head[i]*-5
    # mass.append((Walls_Control(Wall(Physics_polygon(Point(300,200),cat,(0, 255, 0), 0, Point(0, 0), 0)))))
    mass.append(Snake_Control1(Snake(Physics_polygon(Point(randrange(5, screen_size[0]-5, 20),
                                             randrange(5, screen_size[1]-5)),cat_head
                                                     , (0, 255, 0), 1, Point(2, 0), 1),
                                      Point(5, 5), color_Falt), Buttons(pygame.K_a, pygame.K_d)))

    #full cat
    cat = [Point(1, 1), Point(4, 1), Point(4, 3), Point(3, 3), Point(3, 4), Point(5, 4), Point(5, -4),
           Point(4, -4), Point(4, -2), Point(3, -2), Point(3, -4), Point(2, -4), Point(2, -1), Point(0, -1),
           Point(0, -4), Point(-1, -4), Point(-1, -2), Point(-2, -2), Point(-2, -4), Point(-3, -4), Point(-3, 0)
        , Point(-5, 1), Point(-5, 3), Point(-4, 4), Point(-3, 3), Point(-1, 3), Point(0, 4), Point(1, 3)]
    for i in range(len(cat)):
        cat[i] = cat[i] * -10

    mass.append(Snake_Control1(Snake(Physics_polygon(Point(randrange(5, screen_size[0]-5, 20),
                                             randrange(5, screen_size[1]-5)), cat
                                                      , (0, 255, 0), 1, Point(2, 0), 1),
                                      Point(screen_size[0]-80, 5), color_Russia),
                               Buttons(pygame.K_v, pygame.K_b)))

    #star snake и star wall
    star=[Point(0, 4), Point(0, -4), Point(0, 0),Point(4, 0),Point(-4, 0), Point(0, 0)]
    for i in range(len(star)):
        star[i]=star[i]*-6
    # mass.append((Walls_Control(Wall(Physics_polygon(Point(100,100),star,(0, 255, 0), 0, Point(0, 0), 0)))))
    mass.append(Snake_Control1(Snake(Physics_polygon(Point(randrange(5, screen_size[0]-5, 20),
                                             randrange(5, screen_size[1]-5)),star
                                                     , (0, 255, 0), 1, Point(2, 0), 1),
                                      Point(5, 570), color_gum), Buttons(pygame.K_LEFT, pygame.K_RIGHT)))
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

    mass.append(Apples_Control([],'apples_scene_0.csv'))
    mass.append(Walls_Control([],'walls_scene_0.csv'))
    return [mass,screen_size]
