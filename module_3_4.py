# 20.07

def same_root_words(root_word, *other_words):
    words = [*other_words]
    words_family = []
    for i in words:
        if i.lower().find(root_word.lower()) != -1 or root_word.lower().find(i.lower()) != -1:
            words_family.append(i)
    return words_family


result1 = same_root_words('Able', 'disable', 'unable', 'enable', 'fable', 'sable')
result2 = same_root_words('Andalusia', 'andalusian', 'andaluces', 'spanish')

print(result1)
print(result2)


