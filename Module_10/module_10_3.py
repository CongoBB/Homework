import random
from threading import Lock, Thread
from time import sleep


class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            money = random.randint(50, 500)
            self.balance = self.balance + money
            print(f'Пополнение на: {money}, текущий баланс: {self.balance}.')
            sleep(0.001)

    def take(self):
        for i in range(100):
            money = random.randint(50, 500)
            print(f'Запрос на снятие суммы :{money}')
            if money <= self.balance:
                self.balance = self.balance - money
                print(f'Снятие суммы:{money}. Остаток на счете: {self.balance}.')
            elif money >= self.balance:
                print('Запрос отклонён, недостаточно средств!')
                self.lock.acquire()


vtb = Bank(0)

th1 = Thread(target=Bank.deposit, args=(vtb,))
th2 = Thread(target=Bank.take, args=(vtb,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {vtb.balance}')
