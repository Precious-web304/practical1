# store items
items = {
    "clothes": 10,
    "shoes": 20,
    "accessory": 30
}

money = 2000
total_spent = 0
receipt = []

name = input("Enter your name: ")

while True:
    print("\nAvailable Items:")
    for item, price in items.items():
        print(item, "-", price)

    choice = input("\nEnter item (or 'exit'): ").lower()

    if choice == "exit":
        break

    if choice in items:
        quantity = int(input("How many do you want? "))

        cost = items[choice] * quantity

        if cost <= money:
            money -= cost
            total_spent += cost

            receipt.append(
                str(quantity) + " " + choice + " = $" + str(cost)
            )

            print("Purchase successful")
        else:
            print("Insufficient funds")
    else:
        print("Item not found")
#receipt data
print("\n----- RECEIPT -----")
print("Customer:", name)

for item in receipt:
    print(item)

print("\nTotal Spent: $", total_spent)
print("Balance Left: $", money)