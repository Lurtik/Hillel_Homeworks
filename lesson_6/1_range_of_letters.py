from string import ascii_letters

letters = input("Enter a range of letters: ").split("-")
alphabet = ascii_letters

start = alphabet.index(letters[0])
end = alphabet.index(letters[1])

print(alphabet[start:end + 1])