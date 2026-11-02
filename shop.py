# Items and prices
items = {
    "clothing": 10.0,
    "shoes": 20.0,
    "accessory": 30.0
}
money = 8000.0

username = input("Enter your username: ")

print(f"Welcome {username}! You have ${money:.2f} available to spend.")
print("Available items:")
for item, price in items.items():
    print(f"{item}: ${price:.2f}")

purchases = []
total = 0.0

while True:
    item_to_buy = input("Enter the item you want to buy (or 'exit' to quit): ").lower()
    if item_to_buy == "exit":
        break
    elif item_to_buy in items:
        price = items[item_to_buy]
        quantity = int(input(f"How many {item_to_buy} would you like? "))
        cost = price * quantity
        if quantity <= 0:
            print("Please enter a number greater than zero.")
        elif money >= cost:
            money -= cost
            total += cost
            purchases.append((item_to_buy, quantity))
            print(f"You purchased {quantity} {item_to_buy}. Remaining balance: ${money:.2f}")
        else:
            print("Insufficient funds to purchase this item.")
    else:
        print("Item not found. Please choose a valid item.")

print("__Receipt__")
if purchases:
    for item, quantity in purchases:
        print(f"{item} x {quantity}: ${items[item] * quantity:.2f}")
else:
    print("No items purchased.")
print(f"Total: ${total:.2f}")
print(f"Remaining balance: ${money:.2f}")
