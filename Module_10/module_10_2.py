from time import sleep
from threading import Thread


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        hostiles = 100
        days = 0
        print(f'{self.name}, на нас напали!')
        while hostiles > 0:
            hostiles = hostiles - self.power
            days += 1
            print(f'{self.name} сражается {days} {self.number_checker(days)}, осталось {hostiles} воинов)')
            sleep(1)
            if hostiles < 0:
                hostiles = 0
        print(f'{self.name} одержал победу спустя {days} {self.number_checker(days)}')

    @staticmethod
    def number_checker(days):
        if int(str(days)[-1]) == 1:
            days_str = 'день'
        elif int(str(days)[-1]) in [2, 3, 4]:
            days_str = 'дня'
        else:
            days_str = 'дней'
        result = days_str
        return result


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
