#Let's make a module for a restaurant
print("Hi, welcome to our restaurant")
print("Wanna see the menu, have a good look...")
menu = ["Pizza", "Burger", "Fries", "Sandwich", "Pasta", "Salad", "Ice Cream", "Cake", "Cookies", "Soda", "Croissant", "Muffin", "Cupcake", "Waffle", "Donut"]
your_cart = []
print(menu)
print("What would you like to order?")
order = input(str("Enter your order: "))
if order in menu:
    print("Your order is on the way!")
else:
    print("Sorry, we don't have that item in our menu.")
# what do you want to do now ?
print("What would like to do?")
print("1. Add")
print("2. Remove")
print("3. Update")
print("4. Exit")
choice = input("Enter your choice 1/2/3/4: ")
if choice == "1":
    item = input("Enter the item you want to add: ")
    your_cart.append(item)
    print("Your item has been added to your cart.")
    print(your_cart)
elif choice == "2":
    item = input("Enter the item you want to remove: ")
    if item in your_cart:
        your_cart.remove(item)
        print("Your item has been removed successfully!")
elif choice == "3":
    item = input("Enter the item you want to update: ")
    if item in your_cart:
        new_item = input("Enter the new item: ")
        index = your_cart.index(item)
        your_cart[index] = new_item
        print("Your item has been updated successfully!")
elif choice == "4":
    print("Thank you for visiting our restaurant!")
else:
    print("Invalid choice. Please try again.")