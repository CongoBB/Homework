class Vehicle:
    __COLOR_VARIANTS = ['Blue', 'Green', 'Yellow', 'Purple', 'Orange', 'Pink', 'Black', 'White', 'Gray']

    def __init__(self, owner: str, model: str,  color: str, engine_power: int,):
        self.owner: str = owner
        self.__model: str = model
        self.__engine_power: int = engine_power
        self.__color: str = color

    def get_model(self):
        return print(f'Модель: {self.__model}')

    def get_horsepower(self):
        return print(f'Мощность: {self.__engine_power} л.с.')

    def get_color(self):
        return print(f'Цвет: {self.__color}')

    def print_info(self):
        return self.get_model(), self.get_horsepower(), self.get_color(), print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        if new_color.casefold() in list(i.lower() for i in self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Jimmy', 'Chevrolet Corvette Z06', 'Blue', 659)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Brown')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vovan'

# Проверяем что поменялось
vehicle1.print_info()
