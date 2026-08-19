price = int(input("Введіть ціну: "))
discount = int(input("Введіть знижку (%): "))
print(f'Ціна зі знижкою: {price-(price*(discount/100))}')