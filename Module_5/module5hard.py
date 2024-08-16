from time import sleep


class UrTube:
    current_user = None

    def __init__(self):
        self.users: dict[str, User] = {}
        self.videos: dict[str, Video] = {}

    def register(self, nickname, password, age):
        if nickname not in self.users:
            self.users[nickname] = User(nickname, password, age)
            UrTube.current_user = nickname
        else:
            return print(f'Пользователь {nickname} уже существует')

    def log_in(self, nickname, password):
        if nickname in self.users:
            if hash(password) == self.users[nickname].password:
                UrTube.current_user = nickname
                print(f'Вход выполнен, добро пожаловать, {nickname}')
            else:
                print('Неверный пароль')
        else:
            print('Пользователя с таким именем не существует, пожалуйста, зарегистрируйтесь!')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i.title not in self.videos:
                self.videos[i.title] = i

    def get_videos(self, search):
        search_result = []
        for i in list(self.videos.keys()):
            if search.lower() in i.lower():
                search_result.append(i)
        if not len(search_result):
            return 'Видео не найдено'
        else:
            return search_result

    def watch_video(self, choice):
        if UrTube.current_user and choice in list(self.videos.keys()):
            if self.videos[choice].adult_mode and self.users[UrTube.current_user].age >= 18 or \
                    not self.videos[choice].adult_mode:
                i = self.videos[choice].time_now
                while i < self.videos[choice].duration:
                    sleep(1)
                    i += 1
                    print(f'{choice}: [{i}c]')
                    self.videos[choice].time_now = i
                if self.videos[choice].time_now == self.videos[choice].duration:
                    print('Конец видео')
                    self.videos[choice].time_now = 0
            elif self.videos[choice].adult_mode and self.users[UrTube.current_user].age < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif not UrTube.current_user:
            print('Войдите в систему')
        elif choice not in list(self.videos.keys()):
            print('Такого видео нет')


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.age: int = age
        self.password = hash(password)


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = int(time_now)
        self.adult_mode = adult_mode


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 7, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
