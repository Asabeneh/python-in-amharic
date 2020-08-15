
class Person:
    def __init__(self, first_name, last_name, age,city, country='Ethiopia'):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.city = city
        self.skills = []
    
    def person_info(self):
        return f'I am {self.first_name} {self.last_name} and I am  {self.age} years old. I live in {self.city}, {self.country}'
    def add_skill(self, skill):
        self.skills.append(skill)

# Instantiate 

p1 = Person('Asabeneh', 'Yetayeh', 250,'Addis Ababa')
p2 = Person('Donald', 'Trump', 72, 'Washington', 'USA')

print(p1.first_name)
print(p1.last_name)
print(p1.age)

print(p2.first_name)
print(p2.last_name)
print(p2.age)

print(p1.country)
print(p2.country)
print(p1.city)
print(p2.city)
print(p2.country)
print(p1.person_info())
print(p2.person_info())
print(p1.skills)

p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')

print(len(p1.skills))
print(p1.skills)
print(p2.skills)

p2.add_skill('Negotiation')
p2.add_skill('Leading')
p2.add_skill('Intemidating')

print(p2.skills)


class Student(Person):
    def __init__(self,first_name, last_name, age,city, country, gender='male'):
        self.gender = gender
        super().__init__(first_name, last_name, age,city, country)
    def person_info(self):
         gender = 'He' if self.gender =='male' else 'She'
         return f'{self.first_name} {self.last_name} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'



s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')

skills = ['HTML', 'CSS','JS','React','Python','D3.js']

for skill in skills:
    s1.add_skill(skill)

print(s1.person_info())
print('John skills', s1.skills)
print(s2.person_info())




