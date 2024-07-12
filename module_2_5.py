def get_matrix(n, m, value):
    matrix = list([] for i in range(n))
    for i in range(n):
        matrix[i] = list(range(m))
        for j in range(m):
            matrix[i][j] = value
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
answer = input('Would you like to create your own matrix?(y/n)\n')
if answer == 'y':
    result4 = get_matrix(int(input('Enter the number of lines\n')), int(input('Enter the number of columns\n')),
                         int(input('Enter the value\n')))
    print(result4)
print('Goodbye!')
