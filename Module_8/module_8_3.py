class IncorrectVin(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_number(numbers):
            self.__numbers = numbers

    @staticmethod
    def __is_valid_vin(vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVin('Некорректный тип данных для номера vin')
        elif not 1000000 <= vin_number <= 9999999:
            raise IncorrectVin(f'Номер "{vin_number}" не входит в диапазон от 1000000 до 9999999')
        else:
            return True

    @staticmethod
    def __is_valid_number(numbers):
        if not isinstance(numbers, str):
            raise IncorrectNumbers('Некорректный тип данных для номеров автомобиля')
        elif len(numbers) != 6:
            raise IncorrectNumbers('Некорректная длина номера')
        else:
            return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVin as exc:
    print(exc.message)
except IncorrectNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVin as exc:
    print(exc.message)
except IncorrectNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVin as exc:
    print(exc.message)
except IncorrectNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
