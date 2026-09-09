def common_elements():
    set1 = set([i for i in range(100) if i % 3 == 0])
    set2 = set([i for i in range(100) if i % 5 == 0])

    return set1 & set2

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

