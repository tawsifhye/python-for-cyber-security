#send an email with content from API
#implement logging
#make sure email creds are not in the script (external json file)
#properly handle all exceptions specifically

#need to use logging, requests, smtplib, json

import requests
import json
import smtplib


URL = 'https://www.themealdb.com/api/json/v1/1/random.php'


with open("creds.json", "r") as f:
    creds = json.load(f)
    f.close()

EMAIL = creds['email']
PASSWORD = creds['password']
RECIPIENT = '' # recipient's email address 


def send_email(content):
    s = smtplib.SMTP('smtp.gmail.com', 587) #Specific for gmail
    s.starttls()
    s.login(EMAIL, PASSWORD)
    s.sendmail(EMAIL, RECIPIENT, f'\n{content}')
    s.quit()

def get_api_content():
    response = requests.get(URL)
    result = response.json()
    result = result['meals'][0]
    meal_name = result['strMeal']
    meal_instruction = result['strInstructions']
    content = f'{meal_name} Making Instruction: {meal_instruction}'
    return content

email_content = get_api_content()
send_email(email_content)