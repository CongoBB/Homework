all_words = dict()
symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']


class WordsFinder:
    def __init__(self, *args):
        self.file_names = args
        self.all_words = self.get_all_words()

    def get_all_words(self):
        for i in self.file_names:
            with open(i, 'r+', encoding='utf-8') as file:
                all_words[i] = file.read()
                for j in symbols:
                    all_words[i] = all_words[i].replace(j, '')
                all_words[i] = all_words[i].lower().split()
        return all_words

    def find(self, word):
        for file_name, words_list in self.all_words.items():
            if word.lower() in words_list:
                return {file_name: words_list.index(word)+1}
            else:
                return 'Такого слова нет ни в одном из файлов'

    def count(self, word):
        counter = 0
        for file_name, words_list in self.all_words.items():
            for i in words_list:
                if word.lower() == i.lower():
                    counter += 1
                    continue
            if counter:
                return {file_name: counter}
            else:
                return 'Такого слова нет ни в одном из файлов'


finder2 = WordsFinder('Shine On You Crazy Diamond.txt')

print(finder2.get_all_words())
print(finder2.find('diamond'))
print(finder2.count('shine'))
