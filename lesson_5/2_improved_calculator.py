operations = "+-/**"

while True:
    calculation = input("Enter your calculation in format (a 'operation' b) / or stop to close the calculator: ")
    if calculation.lower() == "stop":
        break
    calculation = list(calculation.split())
    op = calculation[1]
    result = 0
    if op in operations:
        if op == "+":
            result = int(calculation[0]) + int(calculation[2])
        elif op == "-":
            result = int(calculation[0]) - int(calculation[2])
        elif op == "*":
            result = int(calculation[0]) * int(calculation[2])
        elif op == "/":
            if int(calculation[2]) == 0:
                print("You can't divide by zero")
                continue
            else:
                result = int(calculation[0]) / int(calculation[2])
        elif op == "**":
            result = int(calculation[0]) ** int(calculation[2])
    else:
        print("Invalid operation")
        continue
    print(f"Your result is {result}")
