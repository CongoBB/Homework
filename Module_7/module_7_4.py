class Team:

    def __init__(self, name, num, score, time, tasks):
        self.name = name
        self.num = num
        self.score = score
        self.time = time
        self.tasks = tasks

    def get_result(self, other):
        if self.num > other.num or self.num == other.num and self.time > other.time:
            return f'Результат битвы: победа команды {self.name}!'
        if self.num < other.num or self.num == other.num and self.time < other.time:
            return f'Результат битвы: победа команды {other.name}!'
        else:
            return 'Ничья!'

    def get_all_players(self, other):
        return 'Сегодня в командах %s и %s участвует игроков: %s и %s соответственно.' % (self.name, other.name,
                                                                                         self.num, other.num)

    def get_players(self):
        return 'Участников в команде %s: %s.' % (self.name, self.num)

    def get_tasks(self):
        return 'Количество задач решённых командой {name}: {tasks}.'.format(name=self.name, tasks=self.tasks)

    def get_time(self):
        return 'Время команды {}: {}с!'.format(self.name, round(self.time, 2))

    def get_total_tasks(self, other):
        return f'Сегодня было решено {self.tasks + other.tasks} задач, среднее время решения задачи: ' \
               f'{round((self.time + other.time)/(self.tasks + other.tasks), 1)}с!'

    def get_all_tasks(self, other):
        return f'Команды {self.name}, {other.name} выполнили {self.tasks} и {other.tasks} задач соответственно.'


t1 = Team('"Мастера кода"', 5, 49, 1552.512, 40)
t2 = Team('"Волшебники данных"', 6, 42, 2153.31451, 42)

print(Team.get_result(t1, t2))
print(t1.get_players())
print(Team.get_all_players(t1, t2))
print(t2.get_tasks())
print(t1.get_all_tasks(t2))
print(Team.get_total_tasks(t1, t2))
print(t1.get_time())
