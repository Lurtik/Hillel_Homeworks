num = input("Enter a number: ")

while True:
    if "0" in num:
        print(0)
        break
    if len(num) == 1:
        print(num)
        break
    res = 1
    for i in num:
        res *= int(i)
    num = str(res)