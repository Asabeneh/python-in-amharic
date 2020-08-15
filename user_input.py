
birth_year = int(input('Enter your bith year: '))
print(type(birth_year))
current_year = int(input('Enter the current year:'))
age = current_year - birth_year

statement = f'You are {age} years old.'
print(statement)


mass = float(input('Enter your mass:'))
gravity = 9.81

weight = mass * gravity
weight = round(weight, 1)
statement = f'Your weight on planet earth is {weight} N.'
print(statement)
