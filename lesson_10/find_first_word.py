from string import punctuation, whitespace

def first_word(text):
    """ Пошук першого слова """

    remove_punctuation = punctuation + whitespace
    text = text.strip(remove_punctuation)

    for i in range(len(text)):
        if text[i] in (remove_punctuation.replace("'", "")):
            return text[:i]
    return text

print(first_word("Hello, world'"))
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
