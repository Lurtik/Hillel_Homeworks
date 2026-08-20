my_list = list(input('Запишіть елементи списку: ').split())
length_list = len(my_list)
mid = length_list // 2
if length_list == 0:
    print(my_list:=[[],[]])
elif length_list % 2 == 0:
    print(my_list := [my_list[:mid],my_list[mid:]])
else:
    print(my_list := [my_list[:mid+1],my_list[mid+1:]])

