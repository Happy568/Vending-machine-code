def vending_machine():

    inventory = {
        "chips": {"price": 1.5, "stock": 10},
        "soda": {"price": 1.0, "stock": 8},
        "chocolate": {"price": 2.0, "stock": 5},
        "water": {"price": 0.75, "stock": 15},
    }

    def display_inventory():
        print("\nCurrent Inventory:")
        for item, details in inventory.items():
            print(f"- {item.title()}: ${details['price']} ({details['stock']} in stock)")

    def calculate_change(balance, price):
        return round(balance - price, 2)

    print("Welcome to the Vending Machine!")

    see_inventory = input("Would you like to see our current inventory? (Yes/No): ").strip().lower()
    if see_inventory != "yes":
        print("Thank you for visiting. Goodbye!")
        return

    while True:
        display_inventory()
        product_name = input("\nEnter the name of the product you want to buy: ").strip().lower()

        if product_name not in inventory:
            print("Product not found. Please try again.")
            continue

        product = inventory[product_name]

        if product["stock"] <= 0:
            print("Sorry, that product is out of stock. Please choose another item.")
            continue

        while True:
            try:
                balance = float(input(f"The price of {product_name} is ${product['price']}. Enter your payment amount: $"))
                if balance < product["price"]:
                    print("Insufficient balance. Please add more money.")
                else:
                    change = calculate_change(balance, product["price"])
                    print(f"Transaction successful! Your change is: ${change}")
                    product["stock"] -= 1
                    break
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

        another_purchase = input("Would you like to buy anything else? (Yes/No): ").strip().lower()
        if another_purchase != "yes":
            print("Thank you for using the vending machine. Have a great day!")
            break

vending_machine()