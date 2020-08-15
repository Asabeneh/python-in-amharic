# Built-in functions:print(), len(), max(), min(), sum(), abs() ....

print('Hello', 'world', 2020)

sentence = 'Everybody in here is enjoying python programing.'

first_name = 'Asabeneh'
print(len(first_name))
print(len(sentence))

print(max(10, 20, 30))
print(max(-1, -20, -30, 0))
print(min(-1, -20, -30, 0))
print(sum([10, 20, 30]))
print(abs(-1))
print(pow(3, 4))  # 3^2 = 3  * 3

# 2a + 3b - a + 1b = a + 4b

gravity = 9.81
sent = 'The gravity of earth is ' + str(gravity)
print(sent)

# Let's see type method to check the data type of a value

a = 10
pi = 3.14
planet = 'Earth'
numbers = [1, 2, 3, 4, 5]
are_you_enjoying = True
is_rainy = False
print(type(a))
print(type(pi))
print(type(planet))
print(type(numbers))
print(are_you_enjoying)
print(type(is_rainy))
