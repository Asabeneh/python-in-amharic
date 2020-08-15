#  Conditionals

x = 0

if x > 0:
    print('The number is greater than 0')
elif x == 0:
    print('The number is zero.')
else:
    print('The number is negative')


userInput = input('Enter value:')
weather = userInput.lower()

if weather == 'rainy':
    print('Please, take your raincoat.')
elif weather == 'foggy':
    print('The day seems very foggy')
elif weather == 'cloudy':
    print('The weather is gloomy and cloudy')
elif weather == 'sunny':
    print('Go out freely, the day seems very shiny')
else:
    print('No one knows about the day')


# Conditionals if, if else, if elif else

'''
age = int(input('Enter your age: '))
if age >= 18 :
    print('You are old enough to drive.')
else:
    years_left = 18 - age

    print(f'You are left with {years_left} years to drive.')
'''
