class House:
    Houses_history = []
    instance = None

    def __new__(cls, name, floors):
        cls.instance = super().__new__(cls)
        cls.Houses_history.append(name)
        return cls.instance

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __del__(self):
        print(f'{self.name} снесён, но останется в истории.')

    def go_to(self, new_floor):
        if self.floors < new_floor or new_floor < 1:
            print(f'\nВ доме {self.name} {new_floor} этажа нет.\n')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.floors}.'

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

h1 = House('Санаторий "Солнечный"', 5)
print(House.Houses_history)
h2 = House('№22', 21)
print(House.Houses_history)
h3 = House('ТРЦ "Победа"', 4)
print(House.Houses_history)

del h2
del h3

print(House.Houses_history)
