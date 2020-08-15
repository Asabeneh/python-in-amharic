
def calc_cube(n, func):
    return func(2) * n


def calc_square(n):
    return n ** 2


print(calc_square(2))
print(calc_cube(2, calc_square))

# map, filter, reduce
# [1, 2, 3] => [2, 4, 6]

nums = [0, 1,  2, 3, 4, 5,  6]


doulbed_nums = list(map(lambda x: x ** 2, nums))
print(doulbed_nums)

even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)

import functools

total = functools.reduce(lambda curr, acc: curr + acc, nums)
print(total)






