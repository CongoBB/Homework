from math import pi, sqrt


class Figure:
    def __init__(self, color: tuple, filled: bool, *sides):
        self.__color: tuple = color
        self.filled: bool = filled
        if isinstance(self, Triangle):
            if len(sides) == 3:
                self.__sides = [*sides]
            else:
                self.__sides = [1 for _ in range(3)]
        elif isinstance(self, Cube):
            if len(sides) == 1:
                self.__sides = [sides[0] for _ in range(12)]
            else:
                self.__sides = [1 for _ in range(self.sides_count)]
        elif isinstance(self, Circle):
            if len(sides) == 1:
                self.__sides = [sides[0]]
            else:
                self.__sides = [1]

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if self.r < 0 or self.g < 0 or self.b < 0 or self.r > 255 or self.g > 255 or self.b > 255 or \
                not isinstance(r, int) or not isinstance(g, int) or not isinstance(b, int):
            return False
        else:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        if not self.__is_valid_color(r, g, b):
            return print('Такого цвета не существует')

    def __is_valid_sides(self, *sides):
        if all([i > 0 for i in [*sides]]) and all([isinstance(i, int) for i in [*sides]]):
            if isinstance(self, Circle):
                if len([*sides]) == self.sides_count:
                    return True
                else:
                    return False
            if isinstance(self, Triangle):
                if len([*sides]) == self.sides_count:
                    return True
                else:
                    return False
            if isinstance(self, Cube):
                if len([*sides]) == 1:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            if isinstance(self, Circle):
                self.__sides = [new_sides[0]]
            elif isinstance(self, Triangle):
                self.__sides = list(new_sides)
            elif isinstance(self, Cube):
                self.__sides = [[*new_sides][0] for _ in range(self.sides_count)]
            return

    def __len__(self):
        if isinstance(self, Circle):
            return self.get_sides()[0]
        elif isinstance(self, Triangle):
            return sum(self.get_sides())
        elif isinstance(self, Cube):
            return self.get_sides()[0] * 12


class Circle(Figure):
    def __init__(self,  color, filled, *sides):
        Figure.__init__(self, color, filled, *sides)
        self.sides_count = 1
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        return self.get_sides()[0]**2 / (4 * pi)


class Triangle(Figure):
    def __init__(self,  color, filled, *sides):
        Figure.__init__(self, color, filled, *sides)
        self.sides_count = 3
        a_ = self.get_sides()[0]
        b_ = self.get_sides()[1]
        c_ = self.get_sides()[2]
        if (a_ + b_) < c_ or (a_ + c_) < b_ or (b_ + c_) < a_:
            print('Треугольника с такими сторонами не существует')
            exit()

    def get_square(self):
        p = self.__len__() / 2
        a_ = self.get_sides()[0]
        b_ = self.get_sides()[1]
        c_ = self.get_sides()[2]
        return (p * (p - a_) * (p - b_) * (p - c_)) ** 0.5


class Cube(Figure):
    def __init__(self,  color, filled, *sides):
        Figure.__init__(self, color, filled, *sides)
        self.sides_count = 12

    def get_square(self):
        return 6 * self.get_sides()[0] ** 2

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), False, 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), True, 6)

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
