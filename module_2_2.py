print('Введите три числа для их сравнения')
first = int(input('Первое число: '))
second = int(input('Второе число: '))
third = int(input('Третье число: '))
if first == second or first == third or second == third:
    if first == second == third:
        k = 3
    else:
        k = 2
else:
    k = 0
if k==0:
    print(f'Вы ввели {k} равных чисел.')
else:
    print(f'Вы ввели {k} равных числа.')
