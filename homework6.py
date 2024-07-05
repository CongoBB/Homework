# 05.07
# словари
my_dict = {'Alex': 'Canada', 'Joshua': 'USA', 'Vladimir': 'Russian Federation', 'Jamal': 'Angola'}  # native country
print(my_dict)
print(my_dict.get('Alex'))
print(my_dict.get('Robert', 'no info'))
my_dict.update({'Jack': 'Norway', 'Kim': 'Sweden'})
print(my_dict)
x = my_dict.pop('Joshua')
print(x)
print(my_dict)

# множества
my_set = {3, 5, 2, 'banana', 0, '1', True, 'banana', 3, 3, 3}
print(my_set)
my_set.update({43, 55})
my_set.add(4.4)
my_set.remove(3)
my_set.discard(44444)
print(my_set)
