num1 = input('Please Enter Number1: ')
num2 = input('Please Enter Number2: ')



try:
    
    num1 = int(num1)
    num2 = int(num2)

    if num1 > num2:
        print(f'{num1} is grater than {num2}')

    elif num1 < num2:
        print(f'{num2} is grater than {num1}')

    else:
        print('Numbers are equal')
except:
    print('Invalid inputs, enter again')