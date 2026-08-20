operations = ["+", "-", "*", "/"]

a, op, b =  input("Введіть операцію у форматі: a оператор b, де оператор один з + - * /\n"
    "Приклад: 3 + 5\n> ").split()
a, b = int(a), int(b)

if op in operations:
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    else:
        print(a / b)
else:
    raise ValueError(f"Немає такої операції {op} у моєму калькуляторі")