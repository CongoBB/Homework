from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'a+') as file:
        for i in range(1, word_count):
            file.write(f'Слово №{i}\n')
            # print(f'В файл {file.name} записываем слово №{i}')
            sleep(0.1)
    return f'Запись в файл {file_name} завершена'


no_thread_time_start = datetime.now()

print(write_words(10, 'example1.txt'))
print(write_words(30, 'example2.txt'))
print(write_words(200, 'example3.txt'))
print(write_words(100, 'example4.txt'))

no_thread_time_end = datetime.now()
print(f'Время затраченное на выполнение программы без использования многопоточности: '
      f'{no_thread_time_end - no_thread_time_start}')

with_thread_time_start = datetime.now()

thread_example_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread_example_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread_example_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread_example_4 = Thread(target=write_words, args=(100, 'example8.txt'))

thread_example_1.start()
thread_example_2.start()
thread_example_3.start()
thread_example_4.start()

thread_example_1.join()
thread_example_2.join()
thread_example_3.join()
thread_example_4.join()

with_thread_time_end = datetime.now()
print(f'Время затраченное на выполнение программы с использованием многопоточности: '
      f'{with_thread_time_end - with_thread_time_start}')
