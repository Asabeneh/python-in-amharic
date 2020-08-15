import numpy
import webbrowser
import requests


lst = [1, 2, 3, 4, 5]
print('this is list', lst)
np_arr = numpy.array(lst)

print('numpy array', np_arr)

lst_times_by_2 = np_arr * 2
print(lst_times_by_2)

url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://twitter.com/Asabeneh',
    'https://github.com/Asabeneh',
]

url = 'https://restcountries.eu/rest/v2/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response)  # response object
print(response.status_code)  # status code, success:200
countries = response.json()
# we sliced only the first country, remove the slicing to see all countries
print(countries[:1])

# JSON -> JavaScript Object Notation






