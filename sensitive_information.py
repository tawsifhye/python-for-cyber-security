import json

with open('credentials.json', 'r') as cred_file:
    data = json.load(cred_file)

    cred_file.close()


email = data['email_credentials']['email']
print(email)