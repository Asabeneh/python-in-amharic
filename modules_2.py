import os
from random import randint, random
import math


print(math.floor(random() * 11))  # 0 to 0.9999 => 0 => 10.999

# generate a list of 7 random numbers





def generate_list_nums ():
    nums = []
    for i in range(7):
        rand_num = math.floor(random() * 11)
        nums.append(rand_num)
    return nums
print(generate_list_nums())

print(randint(5, 10))