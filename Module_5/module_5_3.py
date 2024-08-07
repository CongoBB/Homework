class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def go_to(self, new_floor):
        if self.floors < new_floor or new_floor < 1:
            print(f'\nВ доме {self.name} {new_floor} этажа нет\n')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors

    def __add__(self, value):
        if isinstance(value, House):
            self.floors = self.floors + value.floors
        elif isinstance(value, int):
            self.floors = self.floors + value
        return self

    def __radd__(self, value):
        self.__add__(value)
        return self

    def __iadd__(self, value):
        if isinstance(value, House):
            self.floors += value.floors
        elif isinstance(value, int):
            self.floors += value
        return self


print()

h1 = House('ЖК "Пехра"', 10)
h2 = House('№22', 20)

# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)

print(h1)
print(h2)


print(h1 == h2)

h1 = h1 + 10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)


# h1.go_to(-1)
# h1.go_to(4)
# h2.go_to(22)
# h2.go_to(2)
#
# h3 = House(input('\nВведите название дома:\n'), int(input('Введите количество этажей:\n')))
# h3.go_to(int(input('На какой этаж Вы желаете отправиться?\n')))


#
# print(len(h1))
# print(len(h2))
