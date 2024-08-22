
print("WELCOME TO OUT USELESS STORE\n****************************")

item = input("What items are you purchasing? ")
price = float(input(f"What is the price of {item}? "))
quantity = float(input(f"How many {item} are you buying? "))
total = price*quantity
print(f"Added {quantity} {item}'s to Shopping cart\nSubtotal: ${total}")