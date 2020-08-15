names = ['Asabeneh', 'Abebe', 'Kebede']
fruits = ['Banana', 'Papaya', 'Mango', 'Avocado']
countries = ['Finland', 'Sweden', 'Estonia', 'Norway']

numbers = [1, 2, 3, 4, 5, 6, 7, 9, 10]

print(len(numbers))
print(numbers[2])
print(numbers[3])
print(numbers[-2])

lastIndex = len(numbers) - 1
print(numbers[lastIndex])


mixed_values = ['Banana', 10, [1, 2, 3, 4], 9.81, 3.14, True, 2020]

shoppingList = ['Banana', 'Milk', 'Honey', 'Meat', 'Coffee', 'Apple']
print(shoppingList)
shoppingList[0] = 'Orange'
print(shoppingList)
shoppingList[2] = 'Sugar'
print(shoppingList)

lastIndex = len(shoppingList) - 1
shoppingList[lastIndex] = 'Grape'

print(shoppingList)

list_one = [1, 2, 3, 3]
list_two = [4, 5, 6]


lists = list_one + list_two

print(lists)

# List methods: append, extend, slice,  sort

nums = [1, 2, 3]
print(len(nums))
print(nums)
nums.append(4)
nums.append(5)
print(nums)
nums.extend([6, 7, 8, 9, 10])
print(nums)
nums.insert(5, 0)
print(nums)

fruits = ['Banana', 'Papaya', 'Mango', 'Avocado']
print(fruits)
print(fruits[::-1])

fruits.sort()
print(fruits)

# sort , sorted

countries = ['Finland', 'Sweden', 'Estonia', 'Norway']
sorted_countries = sorted(countries)
print(countries)
print(sorted_countries)

# sort
sorted_countries_2 = countries.sort()
print(sorted_countries_2)
print(countries)
