

# loops
# Repetitive:
# for loop, while

# I want to sum the odd numbers and even numbers separately from 0 to 100


all_evens = 0
all_odds = 0

for x in range(101):
    if x % 2 == 0:
        all_evens = all_evens + x
        print('Even', x)
    else:
        all_odds = all_odds + x
        print('Odd', x)

print('All evens:', all_evens, 'All odds:', all_odds)

nums = [1, 2, 3, 4, 5]  # [2, 4, 6, 8, 10]

new_nums = []

for num in nums:
    new_nums.append(num ** 2)

print(new_nums)

countries = ['Finland', 'Sweden', 'Estonia', 'Norway']


new_countries = []
for country in countries:
    new_countries.append(country.upper())
print(new_countries)


# while loop

x = 0
while x < 6:
    print(x)
    x = x + 1

countries = ['Finland', 'Sweden', 'Estonia', 'Norway']

new_countries = []
for i in range(len(countries), 0, -1):
    new_countries.append(countries[i-1])

print(new_countries)
