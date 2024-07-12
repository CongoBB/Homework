import random
import time

random_number_on_the_wall = random.randint(3, 20)
print(f'The wall shows you this number: {random_number_on_the_wall} \n')
number = int(input('Enter the number you see on the wall\n'))

flag = True
divider = []
while flag:
    i = 3
    while i <= number:
        if number % i == 0:
            divider.append(i)
            i += 1
        else:
            i += 1
    else:
        flag = False

a = []
for i in divider:
    for j in range(1, int(i - i / 2) + 1):
        if j != i - j:
            a.append(j)
            a.append(i - j)
        else:
            break
print('Your program shows you this code: ', ''.join(map(str, a)))
print('You enter the code in the second input field...')


for i in range(3):
    time.sleep(0.5)
    print(' . . . ')
time.sleep(0.5)
if random_number_on_the_wall == number:
    print('You hear a loud rumbling sound')
    time.sleep(0.5)
    print(' . . . ')
    time.sleep(0.5)
    print('The gates have opened!')
else:
    print('You hear a loud metal clank sound')
    time.sleep(0.5)
    print(' . . . ')
    time.sleep(0.5)
    print('YOU DIED')
