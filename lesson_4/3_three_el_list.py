from random import randint

my_random_list = []

for i in range(randint(3, 10)):
    my_random_list.append(randint(0, 10))

print(my_random_list)
print(new_list := [my_random_list[0], my_random_list[2], my_random_list[-2]])
