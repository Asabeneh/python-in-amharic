from pprint import pprint 
empty_dict = {}  # dict()
print(empty_dict)

d = {
    'book': 'መጽሐፍ',
    'flower': 'አበባ',
    'school': 'temehertbet'
}

pprint(d)

print(d['book'])
print(d['flower'])
print(d['school'])


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'city': 'Helsinki',
    'school': 'Helsinki University',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print('What is the length of the dic', len(person))
age = person['age']
print(age)
skills = person['skills']
last_skill = skills[-1]

print(skills)
print(last_skill)

country = person['country']
print(country)


if 'city' in person:
    print(person['city'])
else:
    print('There is not city in the person dictionary')


print(person.get('school'))

person['job'] = 'teaching'
pprint(person)
person['age'] = 150

pprint(person)

'''
person.pop('first_name')
pprint(person)

pprint(len(person))

print('What did we remove using popitem()')
person.popitem()
pprint(person)
print(' after this ')
pprint(len(person))
'''

items = person.items()
pprint(items)
for key in person:
    print(person[key])

keys = person.keys()
print(keys)

values = person.values()

print(values)
