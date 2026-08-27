# [1, 3, 5] => 30
# [6] => 36
# [] => 0

nums_list = [0, 1, 7, 2, 4, 8] #=> (0 + 7 + 4) * 8 = 88

if len(nums_list) == 0:
    print(0)

else:
    res = 0
    for index, value in enumerate(nums_list):
        if index % 2 == 0:
            res += value
    res = res * nums_list[-1]
    print(res)