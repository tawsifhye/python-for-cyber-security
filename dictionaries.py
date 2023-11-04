#key 
#value
# key:value

person = {
    'name': 'Clarke',
    'age': 35,
    'is_employed': True,
    'job': 'mentor',
    'courses': ['C', 'C++', 'Python']
}

# print(person)
print(person['name'])

person['gender'] = 'male'
# print(person)

print(person['courses'][0])

products = [{'name': 'laptop'},{'name':'monitor'},{'name': 'ssd'}]

for product in products:
    print(product['name'])