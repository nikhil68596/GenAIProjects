# Project: Implement Your own Data Structures
inventory = {} #Inventory dictionary

#Functionality to add/remove/or update inventory.
def add_item(item, quantity, value):
    inventory[item] = (quantity, value)

def remove_item(item):
    if item in inventory:
        del inventory[item]

def update_item(item, quan_val):
    if item in inventory:
        inventory[item] = quan_val

#Add two new items to the dictionary to start off with
add_item("apple", 10, 2.5)
add_item("banana", 20, 1.2)
print("Welcome to the Inventory Manager!")
print("\nCurrent inventory:")
def display_inventory():
    for item in inventory:
        quan_val = inventory[item]
        print(f"Item: {item}, Quantity: {quan_val[0]}, Price: ${quan_val[1]}")
    print("")
display_inventory()
#Adding a new item in the inventory
print("Adding a new item: mango")
add_item("mango", 20, 1.2)
print("\nUpdated inventory: ")
display_inventory()

#Remove an item from the inventory
print("Removing an item: apple")
remove_item("apple")
print("\nUpdated inventory: ")
display_inventory()

#Update the quantity or price of an existing item.
print("Updating quantity/price of an item: banana")
update_item("banana", (23, 1.2))
print("\nUpdated inventory: ")
display_inventory()

#Calculate the total value of inventory
total_sum = 0
for item in inventory:
    quan_val = inventory[item]
    total_sum += (quan_val[0] * quan_val[1])
print(f"Total value of inventory: ${total_sum:.2f}")