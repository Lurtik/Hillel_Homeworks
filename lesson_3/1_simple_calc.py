operations = ["+", "-", "*", "/"]

num_1, op, num_2 =  input("Введіть операцію у форматі: a оператор b, де оператор один з + - * /\n"
    "Приклад: 3 + 5\n> ").split()
num_1, num_2 = int(num_1), int(num_2)
if op in operations:
    if op == "+":
        print(num_1 + num_2)
    elif op == "-":
            print(num_1 - num_2)
    elif op == "*":
            print(num_1 * num_2)
    elif op == "/":
        if num_2 == 0:
            raise ZeroDivisionError
        print(num_1 / num_2)
else:
    raise ValueError(f"Немає такої операції {op} у моєму калькуляторі")