import requests

url = 'https://reddit.com/'

c = {
    'test_cookie': 'say something random'
}
h = {
    'User-agent': 'Googlebot'
}

response = requests.get(
    url, 

    )

# code = response.status_code
print(response.text)