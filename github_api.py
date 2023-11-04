import requests
from requests.exceptions import *

token = ''
user = 'tawsifhye'
auth_header = (user, token)
base_url = 'https://api.github.com'

res = requests.get(f'{base_url}/user', auth=auth_header)
print(res.json())