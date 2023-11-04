# Create an inventory tracking system that has all of the following features:

# Each item will have a name, quantity, and description as a dictionary.

# All dictionaries will be saved in a master inventory list.

# A function that adds something to that list (creates the dictionary and adds to the list).

# A function that displays the inventory in a readable format (i.e. do not just print out the list or dictionary, separate them out).

# A function that will change the quantity of an item (this is difficult to do and many ways to do it).

# A function that removes an item from the list. Research required


master_inventory_list = []

def createItem(name, quantity, description):
    item = {
    'name': name,
    'quantity': quantity,
    'description': description
    }
    addToList(item)

def addToList(item):
    master_inventory_list.append(item)

def removeItem(product_name):
    product_found = False
    if len(master_inventory_list) == 0:
        return( print('No Items on the list'))
    else: 
        i = 0
        while i < len(master_inventory_list):
            if(product_name == master_inventory_list[i]['name']):
                master_inventory_list.pop(i)
                product_found = True
                print('After Deleting')
                printInventory()
            i+=1
        if not product_found:
            print('Product not found')



def changeQuantity(product_name, quantity):
    product_found = False
    if len(master_inventory_list) == 0:
        return( print('No Items on the list'))
    
    for product in master_inventory_list:
        if(product_name == product['name']):
            product['quantity'] = quantity
            product_found = True
            print('After Updating')
            printInventory()
            
        if not product_found:
            print('Product not found')

def printInventory():
    for product in master_inventory_list:
        print(f'Product Name: {product['name']}\nQuantity: {product['quantity']}\nDescription: {product['description']}\n-------------')


createItem('Acer Laptop', 3, 'Acer gaming laptop')
createItem('Hp Laptop', 4, 'HP thin laptop')

printInventory()
# removeItem('Laptop')
# printInventory()
changeQuantity('Acer Laptop', 10)