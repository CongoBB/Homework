def calculate_structure_sum(*args):

    first = args[0]
    summ = 0

    if len(args):
        if isinstance(first, int):
            return first + calculate_structure_sum(args[1:])

        if isinstance(first, tuple) or isinstance(first, list) or isinstance(first, dict):
            if len(first):
                if isinstance(first[0], int) or isinstance(first[0], float) and not isinstance(first[0], bool):
                    return first[0] + calculate_structure_sum(first[1:])

                if isinstance(first[0], str):
                    return len(first[0]) + calculate_structure_sum(first[1:])

                if isinstance(first[0], tuple) or isinstance(first[0], list) and first[0]:
                    return calculate_structure_sum(first[0]) + calculate_structure_sum(first[1:])

                if isinstance(first[0], dict):
                    return calculate_structure_sum(list(first[0].keys())) + \
                           calculate_structure_sum(list(first[0].values())) + \
                           calculate_structure_sum(first[1:])

                if isinstance(first[0], set):
                    return calculate_structure_sum(list(first[0])) + calculate_structure_sum(first[1:])

                if isinstance(first[0], bool):
                    return calculate_structure_sum([first[1:]])

    if len(args) == 0:
        return 0

    return summ


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
