#  17.07

def print_params(a=1, b='string', c=True):
    print(a, b, c)
    return


print_params()
print_params(3, '123', False)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 33.4, False]
values_dict = {'a': 65, 'b': 'word', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Route', 66]

print_params(*values_list_2, 'is real')
