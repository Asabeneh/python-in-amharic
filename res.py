
# example.txt, example.py, example.js
# example.xlsx
# example.html
# example.xml
# example.tsv
# example. csv
# example.json

#.txt

# we the builtin open function to open a file
import re
import os

def display_time ():
    from datetime import datetime
    now = datetime.now()                    # 2019-12-04 23:34:46.549883
    day = now.day                   # 4
    month = now.month               # 12
    year = now.year                 # 2019
    hour = now.hour                 # 23
    minute = now.minute             # 38
    second = now.second
    timestamp = now.timestamp()
    return f'{day}/{month}/{year}, {hour}:{minute}'


with open('example.txt', 'r') as f:
    user = os.getlogin()
   
    print('what type is it?', type(f))
    lines = f.readlines()
    print(lines)

    words = []

    for line in lines:
        x = re.findall(r'love', line)
        words = words + x   
# print(f.read())
# print('First line: ',f.readline())
# print(f.readlines())


from datetime import datetime
now = str(datetime.now()).split(' ')[0]
print(now)





a = [1, 2, 3]
b = [4, 5]
c = a + b

print(c)
print(words)

with open('file_writing_example.txt', 'a') as f:
    user = os.getlogin()
    time = display_time()
    f.write(f'4{user}, {time} Learning python will give you the power of doing what ever you want to do.\n')