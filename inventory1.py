class InventoryItem:
      def __init__(self, name, quantity, price):
    self.name = name
    self.quantity = quantity
    self.price = price

def main():
  inventory = []

  while True:
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item Quantity")
    print("4. Remove Item")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      name = input("Enter item name: ")
      quantity = int(input("Enter item quantity: "))
      price = float(input("Enter item price: "))
      inventory.append(InventoryItem(name, quantity, price))
      print(f"{name} added to inventory successfully!")

    elif choice == '2':
      if not inventory:
        print("Inventory is empty!")
      else:
        print("\nInventory List:")
        print("Name\tQuantity\tPrice")
        print("-" * 30)
        for item in inventory:
          print(f"{item.name}\t{item.quantity}\t{item.price:.2f}")

    elif choice == '3':
      if not inventory:
        print("Inventory is empty!")
      else:
        name = input("Enter the name of the item to update: ")
        found = False
        for item in inventory:
          if item.name == name:
            quantity = int(input(f"Enter new quantity for {name}: "))
            item.quantity = quantity
            print(f"Quantity of {name} updated successfully!")
            found = True
            break
        if not found:
          print(f"Item {name} not found in inventory!")

    elif choice == '4':
      if not inventory:
        print("Inventory is empty!")
      else:
        name = input("Enter the name of the item to remove: ")
        found = False
        for i, item in enumerate(inventory):
          if item.name == name:
            del inventory[i]
            print(f"{name} removed from inventory successfully!")
            found = True
            break
        if not found:
          print(f"Item {name} not found in inventory!")

    elif choice == '5':
      print("Exiting Inventory Management System...")
      break

    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
