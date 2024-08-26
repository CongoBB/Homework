string_positions = dict()
file_strings = dict()


def custom_write(file_name, strings):
    file = open(file_name, 'a+', encoding='utf-8')
    for i in strings:
        file_strings[i] = file.tell()
        file.write(f'{i}\n')
    file.close()
    with open('test.txt', 'r') as file:
        for l_no, line in enumerate(file, start=1):
            for i in strings:
                if i in line:
                    string_positions[(l_no, file_strings[i])] = i
                    break
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
