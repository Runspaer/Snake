from Controllers.Objs.Plane.Point import Point
class Simplex:
    def __init__(self, simplex:list,collision_pointers_first:list,collision_pointers_second:list):
        self.simplex=simplex
        self.collision_pointers_first=collision_pointers_first
        self.collision_pointers_second=collision_pointers_second

    def CalculateDirection(self):
        a = self.simplex[-1]
        ao =-a
        if len(self.simplex) == 3:  # Треугольник
            b = self.simplex[1]
            c = self.simplex[0]
            ab = b - a
            ac = c - a
            abPerp =ab.perp()

            # Проверяем направление перпендикуляра, он должен
            # быть направлен против симплекса
            if abPerp * c >= 0:
                abPerp = -abPerp

            #Если начало координат лежит за пределами симплекса, т.е. в направлении перпендкуляра
            #удаляем точку и определяем новое направление в направлении перпендикуляра
            if abPerp * ao > 0:
                self.simplex.pop(0)
                self.collision_pointers_first.pop(0)
                self.collision_pointers_second.pop(0)
                return abPerp
            acPerp =ac.perp()

            # Проверяем направление перпендикуляра, он должен
            # быть направлен против симплекса
            if acPerp * b >= 0:
                acPerp =-acPerp

            # Если начало координат лежит за пределами симплекса, т.е. в направлении перпендкуляра
            # удаляем точку и определяем новое направление в направлении перпендикуляра
            if acPerp * ao > 0:
                self.simplex.pop(1)
                self.collision_pointers_first.pop(1)
                self.collision_pointers_second.pop(1)
                return acPerp

            # Лежит внутри
            return False
        # Не треугольник,т.е. линия
        b = self.simplex[0]
        ab = b - a
        abPerp = ab.perp()

        # Проверяем направление перпендикуляра, он должен
        # быть направлен к началу координат
        if abPerp * ao <= 0:
            abPerp =-abPerp
        return abPerp

    def push_back(self,new_point_simplex: Point,new_point_collision_first,new_point_collision_second):
        self.simplex.append(new_point_simplex)
        self.collision_pointers_first.append(new_point_collision_first)
        self.collision_pointers_second.append(new_point_collision_second)
