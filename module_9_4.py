
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a+') as file:
            for data in data_set:
                file.write(f'{data}' + '\n')
        return
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
# from pprint import pprint
#
#
# with open('example.txt', 'a+') as file:
#     file.seek(0)
#     pprint(file.read())


class MagicBall:
    def __init__(self, question):
        self.answers = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes, definitely.',
                        'You may rely on it.', 'As I see it, yes.', 'Most likely.',
                        'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy try again.', 'Ask again later.',
                        'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.',
                        "Don't count on it.", 'My reply is no.', 'My sources say no.',
                        'Outlook not so good.', 'Very doubtful.']
        if self.__is_valid_question(question):
            self.question = question

    def __is_valid_question(self, question):
        if question:
            self.question = question
            return True
        else:
            return False

    def __call__(self):
        import random
        try:
            return f'{self.question}:\n{random.choice(self.answers)}'
        except AttributeError:
            return 'Ask a question first!\n'


print((question_1 := MagicBall(input("What's your question?\n")))())
print((question_2 := MagicBall(input("What's your question?\n")))())
print((question_3 := MagicBall(input("What's your question?\n")))())
print((question_4 := MagicBall(input("What's your question?\n")))())
