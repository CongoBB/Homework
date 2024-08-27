import os
import datetime
import keyboard


for root, dirs, files in os.walk('.'):
    counter = 0
    for file in files:
        print()
        print(f'Обнаружен файл: {file}.\n'
              f'Путь: {os.path.abspath(file)}.\n'
              f'Время создания файла: '
              f'{datetime.datetime.fromtimestamp(os.stat(file).st_ctime).strftime("%Y-%m-%d %H:%M:%S")}.\n'
              f'Время  последнего изменения файла: '
              f'{datetime.datetime.fromtimestamp(os.stat(file).st_mtime).strftime("%Y-%m-%d %H:%M:%S")}.\n'
              f'Размер файла: {os.stat(file).st_size} байтов.\n'
              f'Родительская директория файла : {os.path.dirname(os.path.abspath(file))}.')
        counter += 1
        print()
        if file == files[-1]:
            print(f'Файлов просмотрено: {counter}, файлов больше нет!')
            exit()
        else:
            print('Для перехода к следующему файлу нажмите "пробел".')
            keyboard.wait('space')
            continue
