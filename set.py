numbers = {0, 1, 2, 3, 3, 4, 5, 'earth', 'potato', 'milk'}  # collections
print(numbers)

for num in numbers:
    print(num)

fruits = ['banana', 'orange', 'mango', 'banana']
print(fruits)

# Set

fruits = ['banana', 'orange', 'mango', 'banana', 'apple', 'apricot']


nums = set()

evens = {0, 2, 4, 6}
whole = {0, 1, 2, 3}

print('evens', evens)
print('whole numbers', whole)

even_union_whole = evens.union(whole)
print(even_union_whole)
even_inter_whole = evens.intersection(whole)
print(even_inter_whole)

even_sym_whole = evens.symmetric_difference(whole)
print(even_sym_whole)  # 4, 6 u 1, 3


new_set = set(fruits)

print(new_set)
print(len(new_set))

companies = set()
print(type(companies))
print(companies)
companies.add('Google')
print(companies)
companies.add('Facebook')
companies.update(['Oracle', 'Apple', 'Microsoft'])

companies.remove('Google')
companies.pop()
# companies.clear()
del companies

nums = {2, 3, 4, 5}
print(4 in nums)
