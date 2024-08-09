# Дополнительное задание №2.
# Создайте список из 10 случайных чисел и напишите функцию для нахождения второго наибольшего числа в этом списке.


import random


random_numbers = [random.randint(-1000, 1000) for i in range(10)]
# random_numbers = [10, 9, 8, 3, 2, 1, 10, 10, 10, 9, 9]   #для проверки
print(random_numbers)


def second_max(random_list):

    lst = random_list
    max_1 = lst[0]
    for i in lst:
        if i > max_1:
            max_1 = i
    while max_1 in lst:
        lst.remove(max_1)
    max_2 = lst[0]
    for i in lst:
        if i > max_2:
            max_2 = i
    return max_2


print(f'{second_max(random_numbers)} - второе наибольшее число в списке случайных значений.')



