def add_everything_up(a, b):
    try:
        summ = a + b
        return round(summ, 3)
    except TypeError:
        summ = f'{a}{b}'
        return summ


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

