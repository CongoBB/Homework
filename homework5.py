# 04.07
immutable_var = 4.07, 2024, 'хлеб', 'молоко', 'яйца', 'лимонад', 'яблоки', 'апельсины', 'бананы'
# пробуем изменить элементы кортежа
try:
    immutable_var[0] = 5.07
    immutable_var[2] = 'черный хлеб'

except TypeError:
    print(type(immutable_var), "contents can't be changed!")  # используется, чтобы пояснить, что это именно кортеж
    # после создания кортежа, значение какого-либо его элемента изменить уже нельзя
    # кортежи неизменяемы(они такими созданы и поэтому называются immutable), в отличие от списков
finally:
    print('Tuple: ', immutable_var)

# проделаем то же самое со списком
mutable_list = [4.07, 2024, 'хлеб', 'молоко', 'яйца', 'лимонад', 'яблоки', 'апельсины', 'бананы']
print('List: ', mutable_list)
mutable_list[0] = 5.07
mutable_list[2] = 'черный хлеб'
print('List with changed contents: ', mutable_list)
