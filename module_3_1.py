#  14.07
calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    string = (len(string), string.upper(), string.lower())
    return string


def does_contain(string, list_to_search):
    count_calls()
    flag = False
    for i in list_to_search:
        if i.lower() == string.lower():
            flag = True
            break
    return flag


print(string_info('Russia'))
print(string_info('Dota'))
print(string_info('Anaesthetist'))
print(string_info('Supercalifragilisticexpialidocious'))   # фантастический, невероятный

print(does_contain('Oxygen', ['Oxy', 'gen', 'water', 'tetraoxygen']))
print(does_contain('Coffee', ['cOFFEe', 'toffee', 'caffeine']))
print(does_contain('Death Stranding', ['Kojima', 'is a Genius', 'Metal GEAR solID', 'deAth sTranDinG']))
print(does_contain('Water', ['H', '2', 'O', 'wAtEr']))
print(does_contain('Dragon', ['LizARD', 'MonSTeR', 'WyVeRn', 'Big DragON', 'Drag', 'On']))

print(calls)
