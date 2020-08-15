
def do_something ():
    print('I am doing something, teaching')

do_something()

# this fun add two numbers
def add_two_nums (a, b):
    total = a + b
    return total

# this fun calculate area of a circle

def calculate_area_circle (radius):
    area = 3.14 * radius ** 2
    return area

# this function generate different length user id

# ab12fgi0


def gen_user_id(n=6):
    import math
    from random import random
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    len_string = len(string)
    id = ''
    for i in range(n):
        rand_index = math.floor(random() * len_string)
        id = id + string[rand_index]
    return id
def calc_factorial (n):
    print('why it is not working')
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f





