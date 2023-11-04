import bcrypt

pw = 'password123'
 
hashed = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()

given = input('Enter a password: ')

is_correct = bcrypt.checkpw(given.encode(), hashed.encode())

if is_correct:
    print("Access Granted")
else:
    print("Access Denied")

