def is_prime(func):
    def wrapper(*args):
        result_wrapper = func(*args)
        if result_wrapper == 2:
            return "Простое число"
        for i in range(2, result_wrapper):
            if result_wrapper % i == 0 or result_wrapper / i ** 0.5 == 0:
                return "Составное число"
        return "Простое число"

    return wrapper


@is_prime
def sum_numbers(*args):
    summ = sum(args)
    print(summ)
    return summ


result = sum_numbers(2, 3, 6)
print(result)
