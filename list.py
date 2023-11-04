fruits = ['banana', 'orange', 'apple']

# for fruit in fruits: 
#     print(fruit)


'''i = 0
while i<len(fruits):
    print(fruits[i])
    i+=1'''

try: 
    user_input_items = int(input('Enter the number of items to store: '))

    i=0
    items = []
    while i< user_input_items:
        item = input('Enter your items name: ')
        items.append(item)
        i+=1

    for item in items:
        print(item)

except:
    print('Enter number only')