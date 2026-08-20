my_list = list(input('Запишіть елементи списку: ').split())
my_list.insert(0, my_list.pop())
print(my_list)