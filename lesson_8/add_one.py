def add_one(come_list: list) -> list:
    come_list = map(str, come_list)
    value = str(int("".join(come_list)) + 1)
    new_value_list = [int(i) for i in value]
    return new_value_list

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
