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


print()

h1 = House('ЖК "Пехра"', 22)
h2 = House('№22', 3)

# h1.go_to(-1)
# h1.go_to(4)
# h2.go_to(22)
# h2.go_to(2)
#
# h3 = House(input('\nВведите название дома:\n'), int(input('Введите количество этажей:\n')))
# h3.go_to(int(input('На какой этаж Вы желаете отправиться?\n')))

print(h1)
print(h2)

print(len(h1))
print(len(h2))
