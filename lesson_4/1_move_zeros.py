# raw_list = [0, 1, 0, 12, 3]
# raw_list = [0]
raw_list = [1, 0, 13, 0, 0, 0, 5]
# raw_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

new_list = [i for i in raw_list if i != 0]
new_list.extend([0] * raw_list.count(0))

print(new_list)