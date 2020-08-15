import re


# match
txt = 'I love to teach python and javaScript'

match = re.match('i LOVE to Teach PYTHON', txt, re.I)
span = match.span()
start = span[0]
end = span[1]
print(start, end)
print(span)
print(match)

phrase = txt[start:end]
print(phrase)

# Search

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for as a first programming language'''

match = re.search('first programming LanguaGE', txt, re.I)
print(match)
start, end = match.span()
print(start, end)

word = txt[start:end]
print(word)

# findall

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

fruits = 'I love apple, banana, orange and other fruits. The wold say goest an apple a day keep the doctor away. Actually, it should be the other way, a banana a day keep the doctor far awar.'

match = re.findall('[Aa]pple|[Bb]anana', fruits)

print(match)
# substitute

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
result = re.sub('[Pp]ython', 'JavaScript', txt)
print(result)

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

result = re.sub('%','', txt)
print('---- The result ----')
print(result)

lines = re.split('\n', result)
print(lines)
print(len(lines))

txt = 'Love is the best thing in this world. Some people talks about love and it is good to love each other. '

pattern = r'love'

matches = re.findall(pattern, txt, re.I)
print(matches)

# pattern = r[A-Z]
txt = 'I was born in 1860 and it has been a wonder time since now in 2020. So for the maximum I can earn is 15000'
pattern = r'[0-9]+'
matches = re.findall(pattern, txt)

print(matches)

# What are the most ten repeated english words
