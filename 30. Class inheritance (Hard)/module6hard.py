#!/usr/bin/python
# coding: utf-8
from math import pi
from math import sqrt


class Figure():
    def __init__(self, __color, __sides, filled=False):
        self.__sides = __sides
        self.__color = __color
        self.sides_count = 0
        self.filled = filled

    def get_color(self):
        return [*self.__color]

    def __is_valid_color(self, *rgb):
        if len(rgb) > 3 and len(rgb) > 0:
            # print("Неправильно количество аргументов цвета!!")
            # print("Пример: (225, 10, 145)")
            return False

        for col in rgb:
            if col < 0 or col > 255:
                # print("Неправильные аргумента параметра rgb")
                # print("Он должен содержать числа от 0 до 255")
                return False

        print("Параметр RGB введен коректно")
        return True

    def set_color(self, *rgb):
        if self.__is_valid_color(*rgb):
            self.__color = (rgb)
            print("Цвет изменен")

    def __is_valid_sides(self,  side_list):
        flag = False

        if len(side_list) != self.sides_count:
            return flag

        for side in side_list:
            if isinstance(side, int) and side > 0:
                flag = True
            if flag == False:
                return flag
        return flag

    def get_sides(self):
        return [self.__sides for i in range(self.sides_count)]

    def __len__(self):
        print(f"Периметр фигуры: {sum(self.__sides)}")
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides) and len(new_sides) == self.sides_count:
            self.__sides = new_sides[0]
        return


class Circle(Figure):
    def __init__(self, color, sides):
        Figure.__init__(self, color, sides)
        self.__radius = sides / (2*pi)
        self.sides_count = 1

    def get_square(self):
        return round(pi * (self.__radius**2), 2)

    def __len__(self):
        return self.get_sides()[0]


class Triangle(Figure):
    def __init__(self, color, sides):
        Figure.__init__(self, color, sides)
        self.sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        semiperimeter = 0.5 * (a + b + c)
        return sqrt(semiperimeter*(semiperimeter-a)*(semiperimeter-b)*(semiperimeter-c))


class Cube(Figure):
    def __init__(self, color, sides):
        Figure.__init__(self, color, sides)
        self.sides_count = 12

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
Triangle1 = Triangle((222, 35, 130), 4)


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
