number = 10

number_by_user = 0
try:
    while number_by_user != number:
        number_by_user = int(input('Please guess a number from 1 to 20: ')) 
        if number_by_user == number:
            print('You have guessed correctly!')

except: 
    print('Enter numeric value only')