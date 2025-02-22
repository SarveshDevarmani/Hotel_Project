print("<-----------------My Python First Project----------------->")

Menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
}
print("Welcome to Five Star Restaurant")
print("Pizza: Rs40\n Pasta: Rs50\n Burger: Rs60\n Salad: Rs70\n Coffee: Rs80 ")

order = 0

order_1 = input("Enter the name of item you want to order= ")
if order_1 in Menu:
    order += Menu[order_1]
    print("Your item has been added to your order")
else:
    print("Ordered item is not available in our restaurant")

order_again = input("Do you want to order something else? (Yes/No)")
if order_again == "Yes":
    order_2 = input("Enter the name of second item: ")
    if order_2 in Menu:
        order += Menu[order_2]
        print("Your item has been added")
    else:
        print("Ordered item is not available yet")

print("The total amount of items to pay is: ",order)
