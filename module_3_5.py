# 20.07


def multiplication(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * multiplication(int(str_number[1:]))
    else:
        return first


result = multiplication(5402462346)
print(result)
