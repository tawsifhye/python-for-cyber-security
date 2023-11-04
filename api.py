import requests
import json

r1 = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
r1 = r1.json()
value1 = r1['meals'][0]['strMeal']
# print(value1)

base_url = 'https://www.themealdb.com/api/json/v1/1/filter.php?a='
query = input('Enter region name to see foods:')

r2 = requests.get(f"{base_url}{query}")
r2 = r2.json()

meals = r2['meals']

for meal in meals:
    print(meal['strMeal'])
