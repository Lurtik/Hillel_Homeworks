from string import punctuation, whitespace

def is_palindrome(sentence: str) -> bool:
    sentence = sentence.lower()
    sentence = [i for i in sentence if i not in (punctuation + whitespace)]
    return sentence == sentence[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("Ok")