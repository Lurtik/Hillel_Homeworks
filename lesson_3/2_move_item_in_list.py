my_list = list(input('Запишіть елементи списку: ').split())
try:
    my_list.insert(0, my_list.pop())
except IndexError:
    pass
print(my_list if len(my_list) != 0 else '[]')