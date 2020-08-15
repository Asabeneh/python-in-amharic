# Strings and String methods

'''
company = 'Coding for all'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())

first_word = company.split()[0]
print(first_word)
# print(company.index('Coding'))
print('Coding' in company)
# Coding For All => Python For All
new_string = company.replace('Coding', 'Python')
print(new_string)

print('Coding For All'.split(' '))

sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)
print(len(sentence))
'''
para = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''

'''
print(para)
letter = 'P'

word = 'Python'
print(len(letter))
print(letter)
print(word)
print(len(word))

first_letter = word[0]
print(first_letter)
two_letters = word[0:2]
print(two_letters)
last_three_chars = word[3:]
print(last_three_chars)
last_char = word[-1]
print(last_char)

# string concatenation
# Asabeneh Yetayeh is a teacher. He lives in Helsinki, Finland. He is 250 years old.

first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'Instructor'
country = 'Finland'
city = 'Helsinki'
age = 250

'''

'''person_info = first_name + ' ' + last_name + ' is an ' + job+ '. He  lives in ' + city+ ', ' + country + '. ' + 'He is ' + str(age) + ' years old.'
print(person_info)'''

'''
person_info = f'{first_name} {last_name} is a {job}. He lives in {city}, {country}. He is {age} years old.'

'''

'''
person_info = '{} {} is a {}. He lives in {}, {}. He is {} years old.'.format(
    first_name, last_name, job, city, country, age)

print(person_info)

some_string = 'Hello'
print(some_string[::-1])
lang = 'Python'
print(lang[0:6:3])

challenge = 'thirty days of python'
print(challenge.capitalize())
print(challenge.upper())
print(challenge.count('th', 0, len(challenge)))

para = 'I love teaching. If you do not love teaching what else can you love. Specially I love teaching programming.'

print(para.count('love', 0, len(para)))
print(para.count('teaching', 0, len(para)))

'''
dna_string = '''TTCCGCAACTGTAGCCCCAAGTCCCTGTAAATGCGGTAGGTTCGCTTGATGTTGGTGCCCCAACCCTCGCGTTCCAAAAGCACATGCACGCGACGATAGCCGTAGCGCACCCG'''

# GC - IDENTIFICATION MARKER gc count

'''
dna_string_len = len(dna_string[5:len(dna_string)-5])
print(dna_string[5:len(dna_string)-5])
number_of_gc = dna_string.count('GC', 0, len(dna_string)) * 2

gc_percentage = (number_of_gc / dna_string_len) * 100
print(gc_percentage)

print(dna_string.startswith('GC'))
print(dna_string.endswith('g'))
print(dna_string.find('GC'))
print(dna_string.isalnum())

'''





