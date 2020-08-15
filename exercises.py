# Loops
import math
from random import random
for i in range(1, 11, 2):
    print(i)

print('This is coming from the while loop')
count = 0
while count < 11:
    print(count)
    count = count + 1


hash = '#'
for i in range(7):
    hash = hash + '#'
    print(hash)

techs = ['Python', 'NumPy', 'Pandas', 'Data Science', 'AI', 'ML']

for tech in techs:
    print(tech.upper())


for i in range(101):
    if i % 2 == 0:
        print(i)

for i in range(101):
    if i % 2 != 0:
        print(i)


def find_sum_of_all(n):
    total = 0
    for i in range(n+1):
        total = total + i
    return total


print(find_sum_of_all(100))


def find_sum_of_evens_and_odds(n):
    sum_of_evens = 0
    sum_of_odds = 0
    for i in range(101):
        if i % 2 == 0:
            sum_of_evens = sum_of_evens + i
        else:
            sum_of_odds = sum_of_odds + i
    return [sum_of_evens, sum_of_odds]


print(find_sum_of_evens_and_odds(100))

# for i in range (5):
#     print(i)


# lst = [1, 2, 3, 4, 5, 6]
# print(len(lst))

companies = ['Facebook', 'Google', 'Microsoft',
             'Apple', 'IBM', 'Oracle', 'Amazon']

comapnies_with_two_os = []
for company in companies:
    if company.count('o') == 2:
        comapnies_with_two_os.append(company)
print(comapnies_with_two_os)

print(companies)
# companies.sort(reverse=True)
print(companies)

company_copy = sorted(companies)
print(companies)
print(company_copy)


def sum_two_nums(a, b):
    total = a + b
    return total


print(sum_two_nums(2, 3))

# mass, height


def calculate_bmi(mass, height):
    # mass = float(input('Enter you mass: '))
    # height = float(input('Enter you height: '))
    bmi = mass / (height * height)
    print(bmi)
    if bmi >= 30:
        print('You are getting obese')
    elif bmi >= 25 and bmi < 30:
        print('You are over weight')
    elif bmi >= 18.5 and bmi < 25:
        print('You are very fit')
    else:
        print('You are under weight')


calculate_bmi(74, 1.72)

# Quadratic equation: ax2 + bx + c
# x2
# x2 + 1
# x2 + 6x + 9 => no, 1 solution, two solution
# b2 - 4ac = 0 => 1 solution
# b2 - 4ac > 0 => 2 solutions
# b2 - 4ac < 0 => no solution
# x2 +6x + 9 => x +3
# -b +/


def solve_quadratic_eqn(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant == 0:
        soln = (-b + discriminant ** 0.5)/(2 * a)
        return set([soln])
    elif discriminant > 0:
        soln1 = (-b + discriminant ** 0.5)/(2 * a)
        soln2 = (-b - discriminant ** 0.5)/(2 * a)
        return set([soln1, soln2])
    else:
        return set()


print(solve_quadratic_eqn(1, 6, 9))
print(solve_quadratic_eqn(1, 4, 3))  # x2 + 4x + 3


rand_num = math.floor(random() * 11)  # 0 -> 10.99999999
print(rand_num)

print(pi)
# ab12fgi0


def gen_user_id(n=6):
    string = '0123456789abcdefghijklmnopqrstuvwxyz'
    len_string = len(string)
    id = ''

    for i in range(n):
        rand_index = math.floor(random() * len_string)
        id = id + string[rand_index]
    return id


print(gen_user_id())
print(gen_user_id(25))
