"""
Author : Ishara Arachchige
Date : 13/06/2026
Project Name : Inventory Management System
"""

# Task one - create a function called add_inventory_item to enter the inventory details.
inventory = {} # store inventory items as a inventory directory.
item_counter = 1000   # create the item counter from 1000 to generate unique item IDs as a global variable outside the function.
def add_inventory_item():
    global item_counter  # call the global variable to update the item counter

# prompt the required inventory item details for user to enter and store. 
    print("Adding Inventory Item :\n")
    item_name = input("Item Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per Item:$ "))

    item_id = item_counter
    item_counter +=1  # automatically increment the item counter for the next item to be added.

# store the inventory item details in the inventory directory.
    inventory[item_id] = {
        "item_name": item_name,
        "quantity": quantity,
        "price" : price
    }

# display the inventory item details to the user.
    print(f"\nItem Name : {item_name}")
    print(f"\nItem ID : {item_id}")
    print(f"\nQuantity : {quantity}")
    print(f"\nPrice : $ {price}")
    
    return item_name, item_id, quantity, price # return the inventory item details to be used in the next function. 


# Task two - create a fuction called calculate_total_value to calculate the total value.
def calculate_total_value():
    item_name, item_id, quantity, price = add_inventory_item()   # call the add_inventory_item fuction from the previous task to get the inventory information to calcualte. 

    total_value = quantity * price

    print(f"Total Value : $ {total_value:.2f}\n")  # display the total value to the user.
    return total_value    # return the total value to be used in the next function. 

# Task three - create a function called update_inventory to update inventory items that is already in the inventory directory.

def update_inventory(item_id):
# when the item ID is not found in the inventory directory, display a message to the user.
    print("Updating Inventory Item : \n")
    if item_id not in inventory:
        message = f"Item ID {item_id} was not found."
        print(message)
        return (message)

    new_quantity = int(input(f"Item ID {item_id}\nEnter New Quantity : "))
    new_price = float(input(f"Item ID {item_id}\nEnter New Price : $ "))

    inventory[item_id] ["quantity"] = new_quantity
    inventory[item_id] ["price"] = new_price

    update_message = f"\nInventory Updated : Item ID {item_id} has been updated to Quantity : {new_quantity} and Price : $ {new_price :.2f}"
    print(update_message)
    return (update_message)

# task four - create a function called display_inventory to display the updated inventory item details to the user.
def display_inventory(item_id):
    print("Displaying Inventory Items : \n")
    if item_id not in inventory:
        print(f"Item ID {item_id} was not found.")
    else:
        item = inventory[item_id]
        total_value = item["quantity"] * item["price"]

        print(f"Item Name : {item['item_name']}")
        print(f"Item ID : {item_id}")
        print(f"quantity : {item['quantity']}")
        print(f"Price : $ {item['price']:.2f}")
        print(f"Total Value : $ {total_value:.2f}\n")

if __name__ == "__main__":  # run the main program to call the functions created above.
    # Add inventory item
    item_name, item_id, quantity, price = add_inventory_item()

    # Calculate total value
    total_value = calculate_total_value()

    # Update inventory item
    update_message = update_inventory(1000)

    # Display inventory item
    display_inventory(1000)


                