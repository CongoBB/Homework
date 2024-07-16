# 16.07
import re


def send_email(message, recipient, *, sender='university.help@gmail.com'):
    is_right = True
    checker2 = True
    for i in [recipient, sender]:
        match = '@'
        if i.find(match) == -1:
            is_right = False
            break
        else:
            check = [".com", '.ru', '.net']
            for j in check:
                match = j
                checker2 = True
                if i.find(match) != -1:
                    break
                else:
                    checker2 = False
                    continue
        if not checker2:
            is_right = False
    if not is_right:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    if is_right and sender == 'university.help@gmail.com' and recipient != 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    elif is_right and sender != 'university.help@gmail.com' and recipient != sender:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    elif is_right and recipient == sender:
        print('Нельзя отправить письмо самому себе!')

    return


print()
a_message = input('Введите ваше сообщение:\n')
a_sender = input('Введите адрес отправителя:\n')
a_recipient = input('Введите адрес получателя:\n')

for z in [a_sender, a_recipient]:
    if re.search(r'[а-яА-ЯёЁ]', z):
        print('Адрес должен быть написан латиницей')
        break
    else:
        send_email(a_message, a_recipient, sender=a_sender)
    break


# send_email('test', 'test@test.ru')
# print()
# send_email('test', 'test@test.com', sender='test@test.ru')
# print()
# send_email('test', 'test@test.net', sender='test@test.com')
# print()
# send_email('test', 'testtest.com', sender='test@test.ru')
# send_email('test', 'test@test.com', sender='testtest.ru')
# send_email('test', 'test@testcom', sender='test@test.ru')
# send_email('test', 'test@test.com', sender='test@testru')
# send_email('test', 'testtest.com', sender='testtest.com')
# print()
# print()
# send_email('test', 'testtest.net')
# send_email('test', 'test@testcom')
# send_email('test', 'testtest')
# send_email('test', 'test@test. com')
# send_email('test', 'test@test.meme')
# print()
# send_email('test', 'university.help@gmail.com')
