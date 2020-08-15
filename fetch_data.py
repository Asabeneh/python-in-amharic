import requests
import collections
from pprint import pprint
url = 'https://restcountries.eu/rest/v2/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
# print(response)  # response object
# print(response.status_code)  # status code, success:200
# countries = response.json()
# pprint(countries)
countries = response.json()

# sort, sorted
nums = [2, -3, 0, 5, 4]
sorted_nums = sorted(nums)
# print(nums)
# print(sorted_nums)
sorted_countries = sorted(countries, key= lambda country:country['population'])
# pprint(sorted_countries)

ten_most_populated_countries = sorted_countries[-10:]

# print('The ten most populated countries')
# pprint(ten_most_populated_countries)
# print(len(ten_most_populated_countries))


ten_most_most_populated_countries = list(map(lambda country: 
    {
    'name':country['name'], 
    'languages':country['languages'][0]['name'],'population':country['population']
    }, ten_most_populated_countries, ))

# pprint(ten_most_most_populated_countries)

# find out the ten most spoken languages in the world
# languages {language:'English', count:45}

languages = {}

for country in countries:
          for lang in country['languages']:
              name = lang['name']
              if name not in languages:
                  languages[name] = 1
              else:
                  languages[name]+=1

pprint(languages)

# print(list(languages))

items = languages.items()
sorted_items = sorted(items, key=lambda item:item[1])


print('These are the most spoken languages')





ten_most_spoken_langs = []
for key, value in sorted_items[-10:]:
    ten_most_spoken_langs.append((value,key))

ten_most_spoken_langs = sorted(ten_most_spoken_langs, reverse=True)
# pprint(ten_most_spoken_langs)



# starts from here

langs = []
for country in countries:
    languages = country['languages']
    for lang in languages:
        name = lang['name']
        langs.append(name)
print(len(langs))
pprint(langs)


unique_lang = list(set(langs))
print(unique_lang)
print(len(unique_lang))



#print(langs)
# unique_languages=[x for x in langs if x not in used and used.append(x)]


'''
unique_languages = []
for x in langs:
    if x not in unique_languages:
        unique_languages.append(x)

pprint(unique_languages)
print("The number of unique langs: ", len(unique_languages))

'''


#     count+=count.unique_languages()
#     unique_languages= unique_languages.append()
# print(unique_languages)
# print(len(unique_languages))
