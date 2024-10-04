from random import randint
from threading import Thread
from time import sleep
import queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, guest_name):
        self.guest_name = guest_name
        super().__init__()

    def run(self):
        random_time = randint(3, 10)
        sleep(random_time)


class Cafe:

    def __init__(self, *args):
        self.queue = queue.Queue()
        self.tables = [*args]

    def is_a_table_available(self):
        for i in self.tables:
            if i.guest is None:
                return True

    def guests_arrival(self, *guests):
        for a_guest in guests:
            if self.is_a_table_available():
                for a_table in self.tables:
                    if a_table.guest is None:
                        a_table.guest = a_guest.guest_name
                        Guest(a_guest).start()
                        print(f'{a_guest.guest_name} садится за стол под номером {a_table.number}.')
                        break
            elif not self.is_a_table_available():
                self.queue.put(a_guest.guest_name)
                print(f'{a_guest.guest_name} в очереди.')

    def serving_guests(self):
        while not self.queue.empty() or self.is_a_table_available():
            for i in self.tables:
                if i.guest is not None and not Guest(i.guest).is_alive():
                    print(f'{i.guest} заканчивает приём пищи и уходит.\nСтол номер {i.number} теперь свободен')
                    i.guest = None
                if not self.queue.empty():
                    i.guest = self.queue.get()
                    print(f'Как следующий гость в очереди, {i.guest} садится за стол номер {i.number} ')
                    Guest(i.guest).start()


tables = [Table(number) for number in range(1, 6)]

guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Victoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests_list = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guests_arrival(*guests_list)
cafe.serving_guests()
