# Functions

# Function

# it prints full name
def print_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name


print(print_name('Asabeneh', 'Yetayeh'))
print(print_name('Abebe', 'Kebede'))
print(print_name('Tatariw', 'Ayele'))

# it adds two numbers


def add_two_nums(a, b):
    total = a + b
    return total


print(add_two_nums(1, 2))
print(add_two_nums(10, 90))


def doSomething(a, b):
    value = a ** b
    return value


print(doSomething(1, 2))


def print_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name
print(print_name('Asabeneh', 'Yetayeh'))
print(print_name('Abebe', 'Kebede'))
print(print_name('Donald', 'Trump'))


def get_sum_of_odd_and_evens():
    all_evens = 0
    all_odds = 0
    for x in range(101):
        if x % 2 == 0:
            all_evens = all_evens + x
        else:
            all_odds = all_odds + x


def calculate_sum_of_evens(n):
    all_evens = 0
    for x in range(n+1):
        if x % 2 == 0:
            all_evens = all_evens + x
    return all_evens

print(calculate_sum_of_evens(100))
# 5 => 5 * 4 * 3  * 2 * 1

def factorial(n):
    f = 1
    for i in range(1, n+1):
        print(f'{f} * {i} = {f * i}')
        f = f * i
    return f

print(factorial(5))

def add_two_nums(a, b):
    total = a + b
    return total
print(add_two_nums(90, 10))

def square_of_number(n):
    sq = n * n
    return sq

print(square_of_number(3))
print(square_of_number(4))


def find_most_repeated_word(para, substring):
    words = []
    for word in para:
        if substring in word:
            words.append(word)
    return len(words)


para = 'I love teaching. If you do not love teaching what else can you love. Specially I love teaching programming.'.split(
    ' ')
print(para)

print(find_most_repeated_word(para, 'love'))
print(find_most_repeated_word(para, 'teaching'))
print(find_most_repeated_word(para, 'I'))




def print_name(first_name):
    return first_name


print(print_name('Abebe'))
print(print_name('Kebede'))
print(print_name('Anteneh'))


def calculate_grade():
    score = float(input('Enter your score:'))
    if score >= 90:
        print('You grade is A')
    elif score >= 70 and score < 90:
        print('Your grade is B')
    elif score >= 60 and score < 70:
        print('Your grade is C')
    elif score >= 50 and score < 60:
        print('Your grade is D')
    else:
        print('Your grade is F')
