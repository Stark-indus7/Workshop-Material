# This project manages inventory data and tracks stock levels.
# Implement the code here

inventory = {}

def add_item(name, quantity):
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity

def remove_item(name, quantity):
    if name in inventory and inventory[name] >= quantity:
        inventory[name] -= quantity
        if inventory[name] == 0:
            del inventory[name]
    else:
        print(f"Not enough {name} in stock")

def view_inventory():
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

# Example usage
add_item("Laptop", 10)
remove_item("Laptop", 2)
view_inventory()
