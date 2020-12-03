word = input(' Enter a word, please : ')


def int_func(word):
    word = word.lower()
    return word.capitalize()


print(int_func(word))

sentence = input(' Enter a sentence, please : ').split()
final_sen = []
for words in sentence:
    final_sen.append(int_func(words))

print(' '.join(final_sen))

