letter_range = list(input("Enter a range of letters: ").split("-"))
result = []

for i in range(ord(letter_range[0]), ord(letter_range[1])+1):
    result.append(chr(i))

print("".join(result))