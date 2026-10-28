# to purchase items from a web or app with the money available
# items to buy
items = {
    "clothe": 10.0,
    "shoes": 20.0,
    "accessory": 30.0
}
# let the user have money to purchase items from a web or app with the money available
money = 2000
# log in 
username = input("Enter your username: ")
password = input("Enter your password: ")
# check if the user is logged in
if password == "mentors":
    print("Login successful!")
else:
    print("access denied")
    # if the user is logged in, display the items and prices
    print(f"Welcome {username}! You have ${money:.2f} available to spend.")
    # display items and prices
    print("Available items:")
    for item, price in items.items():
        print(f"{item}: ${price}")
    # purchase items
    while True:
        item_to_buy = input("Enter the item you want to buy (or 'exit' to quit): ")
        if item_to_buy == "exit":
            break
        elif item_to_buy in items:
            if money >= items[item_to_buy]:
                money -= items[item_to_buy]
                print(f"You have purchased {item_to_buy}. Remaining balance: ${money:.2f}")
            else:
                print("Insufficient funds to purchase this item.")
        else:
            print("Item not found. Please choose a valid item.")
