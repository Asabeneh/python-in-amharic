from mymodules import calc_factorial

print('This our main file')
print(calc_factorial(5))

# Builtin modules

from math import sqrt, pow, floor, pi, factorial, log


print(pi)
print(round(pi, 2))

gravity = 9.81
print(round(gravity))
print(floor(gravity))
print(factorial(4))  # 4 * 3 * 2 * 1 = 24

print(log(2))
print(pow(2,3))

x = 2 ** 3
print(x)

ages = [28, 30, 32, 30, 29, 45, 40, 29, 55, 33, 28, 29]
print(ages)
print(len(ages))

def calculate_mean (lst):
    total = 0
    for num in lst:
        total = total + num
    m = total/len(lst)
    return m

def calculate_median (lst):
    pass

def calculate_mode(lst):
    pass

def calculate_std (lst):
    pass

def caculate_variance (lst):
    pass

def calculate_percentile (lst):
    pass
def caculate_range(lst):
    pass

import statistics

print(dir(statistics))



print(calculate_mean(ages))
print(statistics.mean(ages))
print(statistics.stdev(ages))
print(statistics.variance(ages))

print('Anything you want')

first_name = 'hi people'
print(first_name)
