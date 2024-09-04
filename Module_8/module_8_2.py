def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы: {i} типа: {type(i)}')
            continue
    return result, incorrect_data


def calc_avg(numbers):
    try:
        summ = personal_sum(numbers)
        ar_avg = summ[0] / (len(numbers) - summ[1])
        return ar_avg
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных.')
        return None


print(f'Результат 1: {calc_avg("1, 2, 3")}')
print(f'Результат 2: {calc_avg([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calc_avg(567)}')
print(f'Результат 4: {calc_avg([42, 15, 36, 13])}')
